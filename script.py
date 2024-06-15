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

def get_distinct_words_from_review_text(reviewText):
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
            if review_stars not in number_reviews_containing_word_given_stars:
                number_reviews_containing_word_given_stars[review_stars] = {}

            number_reviews_containing_word_given_stars[review_stars][word] = number_reviews_containing_word_given_stars[review_stars].get(word, 0) + 1
        
        total_reviews = total_reviews + 1



probability_reviews_containing_word_given_stars = number_reviews_containing_word_given_stars
for [review_stars, number_reviews_containing_word_dict] in probability_reviews_containing_word_given_stars.items():
    total_reviews_with_review_starts = frequency_stars.get(review_stars, 0)

    for word in number_reviews_containing_word_dict.keys():
        number_reviews_containing_word_dict[word] = number_reviews_containing_word_dict[word] / total_reviews_with_review_starts


review = "Needed an upgrade from my io7 haha. Not holding its charge and it was time. Not the type of person that needs the newest toy. If it works why change."
distinct_words = get_distinct_words_from_review_text(review)

print(total_reviews)
print(frequency_stars)

print(len(dictionary_set))

# print(number_reviews_containing_word_given_stars)
print(probability_reviews_containing_word_given_stars)
