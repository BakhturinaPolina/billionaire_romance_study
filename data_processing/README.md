# Romantic Novels Preprocessing and Analysis

This project involves various Python scripts designed to preprocess a dataset of romantic novels. The preprocessing steps use BookNLP and spaCy for efficient text processing, various data protocols for POS categorization, and customized scripts for token aggregation and chapter-wise text organization. 

## Directory Structure

### BookNLP for Romantic Novels Processing
Folder: `BOOK_NLP_preprocessing`

This repository houses a Python script for pre-processing a dataset of romantic novels using BookNLP and spaCy. It prepares the data for subsequent Natural Language Processing (NLP) tasks and analysis.

### Text File Token Aggregator
Folder: `combine_tokens`

This script is designed to aggregate tokens from multiple text files found in a directory and its subdirectories. The tokens are categorized into tokens_all, tokens_noun, tokens_verb_noun, and tokens_adj_noun, and are saved as separate .txt files in the root directory for further use.

### Automated Preprocessing for NLP Tasks
Folder: `creating_data_protocols`

This Python script automates the preprocessing of a large dataset of books for subsequent NLP tasks. This includes lemmatizing tokens, categorizing them based on their POS tags, removal of certain tokens (like character names), and saving them in separate text files for easier access and usage.

### Text Processing and Organization Script: Split Novels by Chapters
Folder: `split_novels_by_chapters`

This Python script is designed to process text files, specifically novels. It reads text from each file, splits the text into chapters, and then saves each chapter as a separate text file, resulting in a well-structured and easily navigable directory. The final structure of processed novels is also saved as a JSON file for easy lookup and reference.

The project is ongoing, and the results of these preprocessing steps will be utilized in future analysis to uncover unique insights from the dataset of romantic novels.
