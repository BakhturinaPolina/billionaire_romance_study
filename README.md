# Billionaire_Romantic_Novels Research Project

This repository contains scripts and resources for a computational analysis project focused on modern romantic novels, with a spotlight on the subgenre of billionaire romance. The project explores the power of distant reading techniques including LDA topic modeling, sentiment analysis, and LIWC to provide insights into the thematic, narrative, and psychological elements of the novels.

The project is the collaborative work of P.B. (https://github.com/BakhturinaPolina) and M.F. P.B. came up with the idea of the project and the hypotheses. P.B. and M.F. both contributed to the collection of the corpus. M.F. proposed the algorithm for splitting the novels. M.F. splitted novels from 13 authors. P.B. splitted the novels from 8 authors. Both P.B. and M.F. proposed the algorithms for the corpus preprocessing according to their own needs. P.B. worked on the LDA part. M.F. worked on the SA and LIWC parts.

## Repository Structure

The repository is organized into four main directories:

1. `data_analysis_and_data_visualization`: Contains scripts for statistical analysis and visualization of the model output.

2. `data_processing`: Includes code for preprocessing a large dataset of books for NLP tasks like lemmatizing tokens, categorizing them based on their POS tags, removing certain types of tokens, and saving them in separate text files.

3. `topic_word_extraction`: Houses scripts to extract the most relevant words for each topic in a pre-trained LDA model, represent them in a table, and save this information to a CSV file.

4. `train_model`: Contains scripts for running an LDA model for topic modeling on a collection of text documents and tuning the hyperparameters of the LDA model.

## Libraries Used

The project leverages several libraries including BookNLP, scikit-learn, VADER, LIWC, SpaCy, and NLTK.

## Contributions

This research aims to enhance the understanding of the sub-genre of billionaire romance and demonstrates the applicability of distant reading in literary analysis. The findings and resources provided in this repository offer potential starting points for future research in computational literature analysis.

