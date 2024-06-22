import re
import opendatasets as od
import json
import random
from sklearn.naive_bayes import MultinomialNB


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
    print('processing review 1')
    review_stars = int(training_review['overall'])
    frequency_stars[review_stars] = frequency_stars.get(review_stars, 0) + 1

    review_text = training_review['reviewText']
    distinct_words = get_distinct_words_from_review_text(review_text)

    for word in distinct_words:
        dictionary_set.add(word)

X_training = []
Y_training = []
for training_review in training_reviews:
    print('processing review 2')
    distinct_words = get_distinct_words_from_review_text(review_text)
    sample = []

    for word in dictionary_set:
        if word in distinct_words:
            sample.append(1)
        else:
            sample.append(0)
    X_training.append(sample)

    review_stars = int(training_review['overall'])
    Y_training.append(review_stars)

# Fit the model:
clf = MultinomialNB()
clf.fit(X, Y_training)


X_testing = []
number_correctly_predicted_reviews = 0
for testing_review in testing_reviews:
    review_text = testing_review['reviewText']
    distinct_words = get_distinct_words_from_review_text(review_text)

    sample = []

    for word in dictionary_set:
        if word in distinct_words:
            sample.append(1)
        else:
            sample.append(0)
    X_testing.append(sample)

    star_prediction = clf.predict([sample])[0]

    print('star_prediction', star_prediction)
    actual_stars = int(testing_review['overall'])
    if star_prediction >= 3 and actual_stars >= 3:
        number_correctly_predicted_reviews = number_correctly_predicted_reviews + 1
    elif star_prediction < 3 and actual_stars < 3:
        number_correctly_predicted_reviews = number_correctly_predicted_reviews + 1

print('number_correctly_predicted_reviews', number_correctly_predicted_reviews)
print('len(testing_reviews)', len(testing_reviews))

