# -*- coding: utf-8 -*-
"""topics_extraction_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j82VUdemATdisRiWxQ_QlMbqN8QGYmyy

The purpose of this Python script is to extract the most relevant words for each topic in a pre-trained Latent Dirichlet Allocation (LDA) model, represent them in a table for review, and then save this information to a CSV file.

The script initially loads the pre-trained LDA model using the joblib library. Then it calls a function named get_top_words to extract the top words associated with each topic from the model. It creates a pandas DataFrame with the top words for each topic, prints this table, and finally saves the DataFrame to a CSV file for further use or analysis.
"""

# Import necessary libraries
import pandas as pd
import joblib

# Specify the path of the pre-trained LDA model and load it
best_model_path = "/content/drive/MyDrive/best_model_cla_verb_nouns.pkl"
lda = joblib.load(best_model_path)

# Use the `get_top_words` helper function to extract the top words for each topic
# The function would likely return a dictionary where keys represent the topic indices and values are lists of top words in each topic
tf_feature_names = tf_vectorizer.get_feature_names_out()
top_words_by_topic = get_top_words(lda, tf_feature_names, n_top_words)

# Create a pandas DataFrame to hold the top words for each topic
# Each row of this DataFrame represents a topic, with the index being the topic number and the columns representing the top words
topics_table = pd.DataFrame(top_words_by_topic)
topics_table.index += 1  # Shift index by 1 to make the topic numbering start from 1 instead of 0

# Print the resulting DataFrame for immediate viewing
print(topics_table)

# Save the DataFrame to a CSV file for future use, setting "Topic" as the label for the index column
# The resulting CSV file will contain each topic on a different row, with columns for the top words in the topic
topics_table.to_csv("/content/drive/MyDrive/topics_romantic_novels_verb_nouns_table.csv", index_label="Topic")

"""This script is intended to extract the top words from each topic in a pre-trained Latent Dirichlet Allocation (LDA) model and save them as a CSV file for further examination and analysis. First, it loads the LDA model using the joblib library, then it extracts the top words for each topic. Finally, it creates a pandas DataFrame to store this information, which is then saved as a CSV file for future reference and examination."""

# Import the required libraries
import pandas as pd
import joblib

# Specify the path of the best LDA model and load it
best_model_path = "/content/drive/MyDrive/best_model_cla_verb_nouns.pkl"
lda = joblib.load(best_model_path)

# Extract the top words for each topic using the helper function `get_top_words`
# This function would return a dictionary where the keys are the topic indices and the values are lists of top words in each topic
tf_feature_names = tf_vectorizer.get_feature_names_out()
top_words_by_topic = get_top_words(lda, tf_feature_names, n_top_words)

# Create a pandas DataFrame to store the topic indices and their corresponding top words
# Each row of this DataFrame represents a topic, with the 'Topic Index' column storing the topic index and the 'Top Words' column storing the top words in the topic
topics_table = pd.DataFrame({'Topic Index': range(1, len(top_words_by_topic) + 1),
                             'Top Words': [', '.join(top_words) for top_words in top_words_by_topic.values()]})

# Save the DataFrame to a CSV file for further analysis and visualization
# The resulting CSV file will have each topic on a separate row, with columns for the topic index and the top words in the topic
topics_table.to_csv("/content/drive/MyDrive/topics_for_verb_nouns_romantic_novels.csv", index=False)