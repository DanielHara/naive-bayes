import re
import opendatasets as od
import json

dataset_url = 'https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews'
od.download(dataset_url)

# Retrieve JSON data from the file
dictionary_set = set()

probabilities_dict = {}

total_reviews = 0
frequency_stars = {}

number_reviews_containing_word_given_stars = {}
number_reviews_containing_word = {}

def get_distinct_words_from_review_text(review_text):
    words = re.split('[^a-zA-Z]', review_text)
    distinct_words = set(map(lambda word: word.lower(), words))

    return distinct_words


with open("amazon-reviews/Cell_Phones_and_Accessories_5.json", "r") as file:
    for line in file:
        review = json.loads(line)

        review_stars = int(review['overall'])
        frequency_stars[review_stars] = frequency_stars.get(review_stars, 0) + 1

        review_text = review['reviewText']
        distinct_words = get_distinct_words_from_review_text(review_text)

        for word in distinct_words:
            dictionary_set.add(word)
        
        for word in distinct_words:
            number_reviews_containing_word[word] = number_reviews_containing_word.get(word, 0) + 1

            if review_stars not in number_reviews_containing_word_given_stars:
                number_reviews_containing_word_given_stars[review_stars] = {}

            number_reviews_containing_word_given_stars[review_stars][word] = number_reviews_containing_word_given_stars[review_stars].get(word, 0) + 1
        
        total_reviews = total_reviews + 1



probability_reviews_containing_word_given_stars = number_reviews_containing_word_given_stars
for [review_stars, number_reviews_containing_word_dict] in probability_reviews_containing_word_given_stars.items():
    total_reviews_with_review_starts = frequency_stars.get(review_stars, 0)

    for word in number_reviews_containing_word_dict.keys():
        # Laplace smoothing
        number_reviews_containing_word_dict[word] = (number_reviews_containing_word_dict[word] + 1)/ (total_reviews_with_review_starts + 2)
    
    for word in dictionary_set:
        if word not in number_reviews_containing_word_dict:
            # Laplace smoothing
            number_reviews_containing_word_dict[word] = 1 / (total_reviews_with_review_starts + 2)


# reviewText = "Just got the very well packaged iPhone in the mail and everything works great. It also came with a charger, and most importantly a sim card tool so I could take out my old sim card and put it into this new refurbished phone."
reviewText = "amazing product"
# reviewText = "bad, terrible, sucks"
# reviewText = "and, or, the"
distinct_words = get_distinct_words_from_review_text(reviewText)


best_probability = 0
star_prediction = 0
# Calculations:
for review_star in range(1, 5 + 1):
    if review_star not in probability_reviews_containing_word_given_stars:
        continue

    probability_reviews_containing_word_dict = probability_reviews_containing_word_given_stars[review_star]

    probability = frequency_stars[review_star] / total_reviews

    for word in dictionary_set:
        if word in distinct_words:
            factor = probability_reviews_containing_word_dict.get(word, 0) / (number_reviews_containing_word[word] / total_reviews)
            probability = probability * factor
        """
        else:
            if (1 - number_reviews_containing_word[word] / total_reviews) != 0:
                factor = (1 - probability_reviews_containing_word_dict.get(word, 0)) / (1 - number_reviews_containing_word[word] / total_reviews)
            else:
                factor = 1
        """

    
    if probability >= best_probability:
        best_probability = probability
        star_prediction = review_star

print('star_prediction', star_prediction)

