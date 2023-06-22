# Romantic Novels Topic Modeling

This project employs various preprocessing techniques inspired by literature, to analyze romantic novels. Natural Language Processing (NLP) and topic modeling methodologies are implemented with the aim to capture various narrative aspects. Three protocols focusing on different parts of speech are used: "All nouns and verbs", "All nouns", and "All nouns and adjectives". The project's current stage indicates the effectiveness of nouns in capturing thematic elements.

The hypothesis suggests a normal distribution of themes when applying a model trained on romantic novels to other texts from the same genre. This is supported by the Multinomial Goodness-of-Fit Test results, aligning with the assumption that texts within a genre typically share common thematic elements.

## Directory Structure

### Topic Word Extraction for LDA Models
Folder: `topic_word_extraction`

This Python script is designed to extract the most relevant words for each topic in a pre-trained Latent Dirichlet Allocation (LDA) model, represent them in a table, and save this information to a CSV file for further analysis.

### Topic Modeling and Hyperparameter Tuning with LDA
Folder: `train_model`

This repository contains Python scripts for running a Latent Dirichlet Allocation (LDA) model for Topic Modeling on a collection of text documents and tuning the hyperparameters of the LDA model.

### Topic Modeling: Data Analysis and Data Visualization
Folder: `data_analysis_and_data_visualization`

This code performs data analysis on the resulted model for topic modeling using various statistical methods including chi-square testing, correlation analysis and plotting visualizations.

Please note, this study is preliminary. Further research is needed to validate findings and fully understand the potential of topic modeling in revealing genre peculiarities.

