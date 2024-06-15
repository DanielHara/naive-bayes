import re
import opendatasets as od
import json

dataset_url = 'https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews'
od.download(dataset_url)

# Retrieve JSON data from the file
dictionary_set = set()

probabilities_dict = {}

frequency_stars = {}
with open("amazon-reviews/Cell_Phones_and_Accessories_5.json", "r") as file:
    for line in file:
        review = json.loads(line)

        review_stars = int(review['overall'])
        frequency_stars[review_stars] = frequency_stars.get(review_stars, 0) + 1

        review_text = review['reviewText']
        words = re.split('[^a-zA-Z0-9]', review_text)

        for word in words:
            dictionary_set.add(word.lower())

print(frequency_stars)

print(len(dictionary_set))
