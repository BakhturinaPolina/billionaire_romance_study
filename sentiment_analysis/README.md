# Sentiment Analysis on Novels

This project utilizes Natural Language Processing (NLP) and sentiment analysis techniques to examine novels. It prepares and processes data, applies the Pollyanna Hypothesis, and depicts story arcs using Vonnegut's theory of basic plots.

## Getting Started

Firstly, make sure that your Google Colab environment is set up and you have access to Google Drive. The original notebook for this project can be found [here](https://colab.research.google.com/drive/19K5xFBSNklgFGEbuvRqJCZMgtkl22HqH).

### Prerequisites

Make sure to install SpaCy and nltk libraries. 

```python
! pip install spacy
! pip install nltk
```

This code also requires the installation of the VaderSentiment library. 

```python
! pip install vaderSentiment
```

### Data Preparation

The data for this project is a set of novel texts divided by chapters, stored in a directory on Google Drive. These texts are then preprocessed, tokenized, lemmatized, and cleaned up from non-alphabetical characters and stop words.

### Sentiment Analysis

The project employs the nltk library's Sentiment Intensity Analyzer to determine the polarity scores of the processed texts. These scores are then used to detect the presence of the Pollyanna effect (a tendency towards positivity) within each novel. 

Moreover, the analysis also examines the diversity of positive and negative terms in the texts.

### Plot Analysis

This project uses Vonnegut's theory of the shape of stories to examine the structure of the analyzed novels. This is accomplished by analyzing the sentiment of every sentence in the novel and plotting their mean compound scores.

## Note

For the detailed steps and the code used in the analysis, please refer to the [Jupyter notebook](https://colab.research.google.com/drive/19K5xFBSNklgFGEbuvRqJCZMgtkl22HqH). Make sure to adjust the path to your specific directory where the text files are stored and adjust any other parameters as necessary.
