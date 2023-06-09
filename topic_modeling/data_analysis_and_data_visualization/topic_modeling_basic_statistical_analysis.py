# -*- coding: utf-8 -*-
"""topic_modeling_basic_statistical_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mowj9ZjrK4xvB9woIppudUoEeRVBc9AP

This code is designed to assess the quality of a Latent Dirichlet Allocation (LDA) topic model. After loading a pre-trained LDA model, the script applies it to a set of documents and calculates a number of metrics that are used to understand the characteristics and effectiveness of the topic model:

    Mean and standard deviation of topic correlations across all pairs of documents.
    Chi-square statistic and p-value to test whether the topics are uniformly distributed across documents.

The final output is a table that summarises these metrics for easy comparison and analysis.

Below is the code with comments:
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pickle
from scipy.stats import chisquare
from matplotlib.table import Table
import seaborn as sns

# Define hyperparameters for LDA model2
n_samples_mod2 = 2000
n_features_mod2 = 281
n_components_mod2 = 15
max_df_mod2 = 0.7
min_df_mod2 = 20

# Specify directories for the text data and the pre-trained model
directory_mod2_texts = "/content/drive/MyDrive/romantic_novels_project(topic_modeling_part)/topics_fin/noun_topics"
directory_mod2 = '/content/drive/MyDrive/romantic_novels_project(topic_modeling_part)/models/best_model_cla_nouns.pkl'

# Load the best model
with open(directory_mod2, "rb") as f:
    lda_loaded = pickle.load(f)

# Define function to load data from specified directory
def load_data(directory):
    data_samples = []
    for path in Path(directory).iterdir():
        if path.is_file() and path.suffix == '.txt':
            with open(path) as f:
                contents = f.read()
                data_samples.append(contents)
    return data_samples

# Function to transform data using CountVectorizer
def get_tfs(data=None, nfeats=None, max_df=None, min_df=None):
    print("Extracting tf features for LDA...")
    tf_vectorizer = CountVectorizer(max_df=max_df, min_df=min_df, max_features=nfeats, stop_words="english")
    tfs = tf_vectorizer.fit_transform(data)
    return tf_vectorizer, tfs

# Define function to calculate Chi-square statistic and other metrics
def calculate_chi_square(model_path, data_samples, n_features, n_components, max_df, min_df):
    with open(model_path, "rb") as f:
        lda_loaded = pickle.load(f)

    # Create a CountVectorizer instance and transform the data samples into a document-term matrix
    tf_vectorizer = CountVectorizer(max_df=max_df, min_df=min_df, max_features=n_features, stop_words="english")
    tfs = tf_vectorizer.fit_transform(data_samples)

    # Apply the LDA model to get the topics distribution for each document
    topics_distribution = lda_loaded.transform(tfs)

    n_samples = topics_distribution.shape[0]

    # Calculate correlation scores between all pairs of documents
    correlation_scores = []
    for i in range(n_samples):
        for j in range(i+1, n_samples):
            correlation = np.corrcoef(topics_distribution[i], topics_distribution[j])[0, 1]
            correlation_scores.append(correlation)

    # Create a scatter plot of correlation scores
    sns.scatterplot(x=range(len(correlation_scores)), y=correlation_scores, alpha=0.5, color="#C79FEF")
    plt.xlabel('Document Pairs')
    plt.ylabel('Correlation Score')
    plt.title('Correlation Scores between Documents')
    plt.show()

    # Calculate mean and standard deviation of the correlation scores
    correlation_mean = np.mean(correlation_scores)
    correlation_std = np.std(correlation_scores)

    # Calculate observed and expected distributions of topics
    observed_distribution = np.sum(topics_distribution, axis=0)
    observed_distribution = observed_distribution / np.sum(observed_distribution)

    expected_distribution = np.full_like(observed_distribution, 1 / n_components)
    expected_distribution = expected_distribution / np.sum(expected_distribution)

    # Perform chi-square test to check if the topics are equally distributed across documents
    chi_square_statistic, p_value = chisquare(observed_distribution, expected_distribution)

    alpha = 0.05
    if p_value < alpha:
        hypothesis_result = "Reject the null hypothesis: Topics are not equally distributed across documents."
    else:
        hypothesis_result = "Fail to reject the null hypothesis: Topics are equally distributed across documents."

    return correlation_mean, correlation_std, chi_square_statistic, p_value, hypothesis_result

# Load the data samples
data_samples_mod2 = load_data(directory_mod2_texts)

# Prepare lists of model paths, data samples, and hyperparameters for processing
model_paths = [directory_mod2]
data_samples_list = [data_samples_mod2]
hyperparameters_list = [
    (n_features_mod2, n_components_mod2, max_df_mod2, min_df_mod2)
]

# Iterate over each model path, data samples, and hyperparameters to calculate metrics and store results
table_data = []
for model_path, data_samples, hyperparameters in zip(model_paths, data_samples_list, hyperparameters_list):
    n_features, n_components, max_df, min_df = hyperparameters
    correlation_mean, correlation_std, chi_square_statistic, p_value, hypothesis_result = calculate_chi_square(model_path, data_samples, n_features, n_components, max_df, min_df)
    table_data.append([correlation_mean, correlation_std, chi_square_statistic, p_value])

# Convert results to a numpy array for display in a table
table_data = np.array(table_data)
table_columns = ["Metric", "Value"]

# Create the table data including labels and values
data_labels = ['Correlation Mean', 'Correlation Std', 'Chi-square Statistic', 'P-value']
table_data = np.vstack((data_labels, table_data)).T

# Plot the table of results
fig, ax = plt.subplots(figsize=(8, 4))
table = ax.table(cellText=table_data, colLabels=table_columns, loc='center')

# Adjust table properties for a clear display
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Hide axes and show the plot
ax.axis('off')
plt.tight_layout()
plt.show()

# Load the data samples
data_samples_mod2 = load_data(directory_mod2_texts)

# Apply CountVectorizer to get the document-term matrix
tf_vectorizer, tfs = get_tfs(data=data_samples_mod2, nfeats=n_features_mod2, max_df=max_df_mod2, min_df=min_df_mod2)

# Apply the LDA model to get the topics distribution for each document
topics_distribution = lda_loaded.transform(tfs)

# Calculate the overall topics distribution by summing across all documents
topics_distribution_sum = np.sum(topics_distribution, axis=0)
topics_distribution_sum = topics_distribution_sum / np.sum(topics_distribution_sum)

# Calculate the expected topics distribution
expected_distribution = np.full_like(topics_distribution_sum, 1 / n_components_mod2)
expected_distribution = expected_distribution / np.sum(expected_distribution)

# Calculate the difference between expected and real topics distribution
difference = topics_distribution_sum - expected_distribution

# Plot the histogram of the difference
sns.set(style="darkgrid")
plt.figure(figsize=(8, 4))
sns.histplot(data=difference, kde=True, color="#C79FEF")
plt.axvline(0, color='r', linestyle='--', label='Expected')
plt.xlabel('Difference')
plt.ylabel('Frequency')
plt.title('Histogram of Difference between Expected and Real Topics Distribution')
plt.legend()
plt.show()