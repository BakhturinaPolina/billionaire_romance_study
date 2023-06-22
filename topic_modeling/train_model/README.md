# Topic Modeling and Hyperparameter Tuning with LDA

This repository contains Python scripts for running a Latent Dirichlet Allocation (LDA) model for Topic Modeling on a collection of text documents and tuning the hyperparameters of the LDA model. 

## Code Overview

The code includes several functions to:

1. Download FastText word vectors and extract feature vectors
2. Compute coherence scores for given top words and for all topics
3. Plot the top words for each topic
4. Transform data using `CountVectorizer`
5. Fit an LDA model to the data
6. Load text data from a directory
7. Search a grid of hyperparameters to find the best model

## Key Features

- **FastText Word Vectors:** The code uses FastText word vectors to compute coherence scores for the topics produced by the LDA model.

- **Grid Search:** The script searches a grid of hyperparameters, including document length, max and min document frequency, number of features, and number of components (topics), to find the best model.

- **Perplexity and Coherence:** The script evaluates the models based on their perplexity and coherence. Perplexity is a measure of how well a model predicts a sample and is commonly used to compare different topic models. Coherence measures the semantic similarity of the top words in each topic and can provide insights into the interpretability of the topics.

- **Visualization:** The code includes a function to plot the top words for each topic, which can help visualize the results of the topic modeling.

## Running the Code

To run the code, you will need a directory of text files (`directory = "/content/drive/MyDrive/high_lit_topics/nokens_noun"`), which will be loaded and transformed into a document-term matrix. The LDA model will then be fit to this matrix. The script will search a grid of hyperparameters to find the best model based on perplexity and coherence.

The best model will be saved as a pickle file, which can be loaded in future runs of the script. The coherence of the best model's topics will be calculated, and the best topic will be identified based on the highest coherence score. The top words for the best topic will be printed out.

## Requirements

- Python 3.6 or above
- sklearn
- numpy
- matplotlib
- gzip
- pathlib
- itertools
- requests
- pickle

## Contributing

Contributions are welcome! 
