import opendatasets as od
import json

dataset_url = 'https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews'
od.download(dataset_url)

# Retrieve JSON data from the file
dictionary_set = set()
with open("amazon-reviews/Cell_Phones_and_Accessories_5.json", "r") as file:
    line = file.readline()
    data = json.loads(line)

    reviewText = data['reviewText']
    words = reviewText.split()
    for word in words:
        dictionary_set.add(word)

print(dictionary_set)
