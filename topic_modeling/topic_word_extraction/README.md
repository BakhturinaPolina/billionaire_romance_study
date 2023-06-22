# Topic Word Extraction for LDA Models

This Python script is designed to extract the most relevant words for each topic in a pre-trained Latent Dirichlet Allocation (LDA) model, represent them in a table, and save this information to a CSV file for further analysis. 

## Dependencies
The code uses the following libraries:
* pandas
* joblib

## Workflow

The script's workflow is outlined below:

### Load Pre-Trained LDA model

The LDA model used in this code is loaded from a pickle file using joblib library.

```python
lda = joblib.load(best_model_path)
```

### Extract Top Words

The script calls the helper function `get_top_words()` to extract the top words associated with each topic from the model.

```python
top_words_by_topic = get_top_words(lda, tf_feature_names, n_top_words)
```

### Create DataFrame

The top words for each topic are then transformed into a pandas DataFrame where each row represents a topic, and the columns represent the top words.

```python
topics_table = pd.DataFrame(top_words_by_topic)
```

### Save to CSV

Finally, the DataFrame is saved to a CSV file for future use, with each topic represented on a different row and the top words in each topic represented in columns.

```python
topics_table.to_csv("/content/drive/MyDrive/topics_romantic_novels_verb_nouns_table.csv", index_label="Topic")
```

## Usage

To use this script, ensure that you have a pre-trained LDA model saved as a pickle file. You should also have a helper function `get_top_words()` which extracts the top words from the LDA model.

Change the `best_model_path` to the path of your LDA model. The CSV file will be saved in the same directory as the script by default, but you can change this by specifying a different path in the `to_csv()` function.

The helper function `get_top_words()` should return a dictionary where keys represent the topic indices, and values are lists of top words in each topic.

## Result

This script helps in analyzing LDA models by extracting the top words for each topic and saving this information for further review and analysis. This is useful in understanding the context and relevance of the identified topics in a more direct and intuitive way.
