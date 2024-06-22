# Text classification with Naive Bayes

I'm trying to learn a bit of Machine Learning by myself, and an interesting approach for text classification is Native Bayes. In this case, I was curious about classifying Amazon reviews into positive (>= 3 stars), and negative (<=2 stars). The used data comes from https://www.kaggle.com/datasets/abdallahwagih/amazon-reviews. My aim was to implement the whole classifier from scratch, so no dependencies like ``scikit-learn``.

# The data
An array that looks like this:

```json
[
  {
     "reviewerID":"A3E4H05JS9IUFI",
     "asin":"B0002EOFFK",
     "reviewerName":"Roger",
     "helpful":[
        0,
        0
     ],
     "reviewText":"This was definitely easy to install. It can be removed and transferred from one vehicle to another. Adds just enough gain to work great.",
     "overall":5.0,
     "summary":"Works great",
     "unixReviewTime":1370908800,
     "reviewTime":"06 11, 2013"
  }
]
```
For the model, the only relevant fields are `reviewText` and `overall`.

# How it works

The naive Bayes model just builds a dictionary for all the words in the training data. For each review, it takes into account only the presence or absence of a word, and doesn't care neither about the position of the words in the sentence, or nor about the presence or absence of other words. That's why it's called naive. I used https://anote-ai.medium.com/naive-bayes-bag-of-words-approach-a-powerful-text-classification-technique-8ccfb07ac2be, https://www.datacamp.com/tutorial/naive-bayes-scikit-learn and https://www.geeksforgeeks.org/gaussian-naive-bayes-using-sklearn/ as references.

# How long to code it?
Just some 3 hours for all, as I'm short of time :)

Just a long script, no optimizations or a lot of attention to code readability.

# What is the result?

In the training set, there are `194339` reviews, and `100` reviews on the testing set. Of the `194339` reviews in the training set, `13271` have 1 star, `11058` have 2 stars, `21425` have 3 stars, `39970` have 4 stars and `108615` have 5 stars.

The naive and simple model I implemented just classifies a review as positive or negative. Out of the `100` reviews, it classified correctly 92 reviews, which sounds good at **first glance**.

As you noticed, 87% of the reviews overall are positive reviews, so if you would build a model which simply classifies every review as a positive review, it'd have correctly classified 87% of the reviews. I'm at 92%, which is already better, but still **not a whole lot better**.

# What did I learn from this?

That a very, very simple model, coded in 3 hours, with no dependencies, can already beat the "educated guess" model (in which the classifier just picks the same classification every time - in this case, always guessing every review is a positive review). It still needs improvement and refinement, but not bad!

# Next steps??

Trying out some of the models from https://levity.ai/blog/text-classifiers-in-machine-learning-a-practical-guide. I'd be interested in K-Nearest Neighbors, for example, given that it's also relatively easy to implement from scratch!

