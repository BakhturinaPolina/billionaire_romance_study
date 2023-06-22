# LIWC Novels Analysis

This is a Python project that uses the Linguistic Inquiry and Word Count (LIWC) method to analyze a set of books in a dataset. The project has been developed as a Jupyter notebook and can be run in Google Colaboratory.

## Project Structure

The project is a Python notebook that includes a set of functions to load and analyze the text files. It starts with mounting the Google drive to access the dataset. The Linguistic Inquiry and Word Count (LIWC) method is applied to analyze the text files. The texts are tokenized and preprocessed by removing punctuations, converting to lowercase, and removing stop words. The LIWC method is applied to identify categories in each chapter and for the entire dataset.

The project structure is as follows:

- Load necessary libraries and mount Google Drive.
- Install and import LIWC library.
- Define the path to the dataset.
- Preprocess the text data (tokenization, removal of punctuations and stopwords).
- Identify the LIWC categories in each chapter and in the whole dataset.
- Count the number of matches for each category.
- Save the output as CSV or JSON files.

## How to Use

1. Clone the repository or download the `liwc_novels.ipynb` notebook.

2. Open the notebook in Google Colaboratory.

3. The project requires the dataset of text files to be stored in Google Drive. Update the path of the dataset in the cell:

```python
rootdir = '/content/drive/MyDrive/billionaire_romance_study/toy_dataset_splitted_with_names'
```

4. The project also requires the LIWC dictionary file. Update the path in the cell:

```python
liwc_path = '/content/drive/MyDrive/billionaire_romance_study/code/LIWC2007_English100131.dic'
```

5. Run all the cells.

6. The final results will be stored as CSV or JSON files in your Google Drive. The name of the output file can be modified as needed.

## Dependencies

The project requires the following Python libraries:

- `liwc`
- `nltk`
- `os`
- `re`
- `json`
- `pandas`
- `string`
- `collections`
- `numpy` (if not already included in your Python environment)

These can be installed with `pip` using the command `pip install <library-name>`.

## Contribution

Feel free to contribute to this project by providing suggestions, reporting issues, or making pull requests. All contributions are welcomed.
