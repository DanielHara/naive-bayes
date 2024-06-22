import re
import opendatasets as od
import json
import random

dataset_url = 'https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews'
od.download(dataset_url)

# Retrieve JSON data from the file
dictionary_set = set()

probabilities_dict = {}

number_total_reviews = 194439
number_training_reviews = number_total_reviews - 100
frequency_stars = {}

number_reviews_containing_word_given_stars = {}
number_reviews_containing_word = {}

def get_distinct_words_from_review_text(review_text):
    words = re.split('[^a-zA-Z]', review_text)
    distinct_words = set(map(lambda word: word.lower(), words))

    return distinct_words

number_read_reviews = 0
reviews = []
with open("amazon-reviews/Cell_Phones_and_Accessories_5.json", "r") as file:
    for line in file:
        review = json.loads(line)

        reviews.append(review)
random.shuffle(reviews)

training_reviews = reviews[0:number_training_reviews]
testing_reviews = reviews[number_training_reviews:]
for training_review in training_reviews:
    review_stars = int(training_review['overall'])
    frequency_stars[review_stars] = frequency_stars.get(review_stars, 0) + 1

    review_text = training_review['reviewText']
    distinct_words = get_distinct_words_from_review_text(review_text)

    for word in distinct_words:
        dictionary_set.add(word)
    
    for word in distinct_words:
        number_reviews_containing_word[word] = number_reviews_containing_word.get(word, 0) + 1

        if review_stars not in number_reviews_containing_word_given_stars:
            number_reviews_containing_word_given_stars[review_stars] = {}

        number_reviews_containing_word_given_stars[review_stars][word] = number_reviews_containing_word_given_stars[review_stars].get(word, 0) + 1



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



number_correctly_predicted_reviews = 0
for testing_review in testing_reviews:
    review_text = testing_review['reviewText']
    distinct_words = get_distinct_words_from_review_text(review_text)

    best_probability = 0
    star_prediction = 0
    # Calculations:
    for review_star in range(1, 5 + 1):
        if review_star not in probability_reviews_containing_word_given_stars:
            continue

        probability_reviews_containing_word_dict = probability_reviews_containing_word_given_stars[review_star]

        probability = frequency_stars[review_star] / number_total_reviews

        for word in dictionary_set:
            if word in distinct_words:
                factor = probability_reviews_containing_word_dict.get(word, 0) / (number_reviews_containing_word[word] / number_total_reviews)
            else:
                factor = (1 - probability_reviews_containing_word_dict.get(word, 0)) / (1 - number_reviews_containing_word[word] / number_total_reviews)            
            
            
            probability = probability * factor
        
        if probability >= best_probability:
            best_probability = probability
            star_prediction = review_star

    actual_stars = int(testing_review['overall'])
    if star_prediction >= 3 and actual_stars >= 3:
        number_correctly_predicted_reviews = number_correctly_predicted_reviews + 1
    elif star_prediction < 3 and actual_stars < 3:
        number_correctly_predicted_reviews = number_correctly_predicted_reviews + 1

print('number_correctly_predicted_reviews', number_correctly_predicted_reviews)
print('len(testing_reviews)', len(testing_reviews))
print('frequency_stars', frequency_stars)

