# Topic Modeling: Data Analysis and Data Visualiation

This code performs data analysis on the resulted model for topic modeling using various statistical methods including chi-square testing, correlation analysis and plotting visualizations.

## Dependencies
The code uses the following libraries:
* numpy
* matplotlib
* sklearn
* pathlib
* pickle
* scipy
* seaborn

## Structure

The project is mainly composed of Python scripts implementing the following functionality:

### Load Pre-Trained LDA model

The LDA model used in this code is loaded from a pickle file.

```python
with open(directory_mod2, "rb") as f:
    lda_loaded = pickle.load(f)
```

### Loading Data

The function `load_data(directory)` is used to load text data from .txt files from the specified directory. 

```python
data_samples_mod2 = load_data(directory_mod2_texts)
```

### Feature Extraction

The function `get_tfs(data=None, nfeats=None, max_df=None, min_df=None)` is used to transform the loaded text data into a document-term matrix, using the `CountVectorizer` class from the sklearn library.

```python
tf_vectorizer, tfs = get_tfs(data=data_samples_mod2, nfeats=n_features_mod2, max_df=max_df_mod2, min_df=min_df_mod2)
```

### Correlation Analysis & Chi-Square Testing

The function `calculate_chi_square(model_path, data_samples, n_features, n_components, max_df, min_df)` calculates chi-square statistics and correlation metrics for the given data and hyperparameters. 

```python
correlation_mean, correlation_std, chi_square_statistic, p_value, hypothesis_result = calculate_chi_square(model_path, data_samples, n_features, n_components, max_df, min_df)
```

### Visualization

Various matplotlib and seaborn plots are used to visualize data correlations, chi-square statistics, and the difference between the expected and real topics distribution.

```python
plt.show()
```

## Usage

You can adjust the hyperparameters and directories to suit your use case. Please ensure the input data is in the form of .txt files placed in the appropriate directory.

## Analysis

This codebase allows to calculate important statistical metrics like correlation between documents, chi-square statistics for topic distribution, and visualize the results. You can see the difference between the expected and real topic distributions in histogram format. This provides a deeper understanding of how well the LDA model is performing and the nature of the topics in your data.

Remember to set your desired hyperparameters and ensure that the text data and pre-trained model are located in the directories specified in your environment.

