# Romantic Novels Analysis Project

This repository contains scripts and resources for a computational analysis project focused on modern romantic novels, with a spotlight on the subgenre of billionaire romance. The project explores the power of distant reading techniques including LDA topic modeling, sentiment analysis, and LIWC to provide insights into the thematic, narrative, and psychological elements of the novels.

The project is the collaborative work of P.B. (https://github.com/BakhturinaPolina) and M.F. P.B. came up with the idea of the project and the hypotheses. P.B. and M.F. both contributed to the collection of the corpus. M.F. proposed the algorithm for splitting the novels. M.F. splitted novels from 13 authors. P.B. splitted the novels from 8 authors. Both P.B. and M.F. proposed the algorithms for the corpus preprocessing according to their own needs. P.B. worked on the LDA part. M.F. worked on the SA and LIWC parts.

This repository contains multiple projects each employing different analysis techniques on a corpus of romantic novels. The projects include Linguistic Inquiry and Word Count (LIWC) analysis, preprocessing of data, sentiment analysis, and topic modeling.

## Repository Structure

### Romantic Novels Preprocessing 
Folder: `data_processing`

Various Python scripts aim to preprocess the dataset of romantic novels. The preprocessing involves efficient text processing with BookNLP and spaCy, POS categorization, token aggregation, and organization of text by chapters.

#### Subfolders:
- `BOOK_NLP_preprocessing`: Scripts for pre-processing romantic novels using BookNLP and spaCy.
- `combine_tokens`: Aggregates tokens from multiple text files, categorized by their type.
- `creating_data_protocols`: Automates preprocessing for NLP tasks.
- `split_novels_by_chapters`: Splits novels into chapters and organizes them into separate text files.

### LIWC Novels Analysis
Folder: `LIWC Novels Analysis`

A Python-based Jupyter notebook project that employs the Linguistic Inquiry and Word Count (LIWC) method to analyze a collection of novels, extracting not only emotions and sentiments but also a wide range of psychological, social, and behavioral phenomena.

### Sentiment Analysis on Novels
Folder: `sentiment_analysis`

A project that applies NLP and sentiment analysis techniques to analyze novels. The approach includes the application of the Pollyanna Hypothesis and representation of story arcs using Vonnegut's theory of basic plots.

### Romantic Novels Topic Modeling
Folder: `topic_modeling`

A project that applies preprocessing techniques inspired by literature to analyze romantic novels using NLP and topic modeling. The analysis focuses on different parts of speech to capture various narrative aspects. 

#### Subfolders:
- `topic_word_extraction`: Extracts the most relevant words for each topic from a pre-trained LDA model.
- `train_model`: Scripts for running an LDA model for Topic Modeling and tuning its hyperparameters.
- `data_analysis_and_data_visualization`: Performs data analysis on the resultant model for topic modeling using various statistical methods.

Please note that these studies are still preliminary. Further research is needed to validate findings and fully understand the potential of these techniques in revealing genre peculiarities.
