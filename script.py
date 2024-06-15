import re
import opendatasets as od
import json

dataset_url = 'https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews'
od.download(dataset_url)

# Retrieve JSON data from the file
dictionary_set = set()
with open("amazon-reviews/Cell_Phones_and_Accessories_5.json", "r") as file:
    for line in file:
        data = json.loads(line)

        reviewText = data['reviewText']
        
        words = re.split('[^a-zA-Z0-9]', reviewText)

        for word in words:
            dictionary_set.add(word.lower())

print(len(dictionary_set))
