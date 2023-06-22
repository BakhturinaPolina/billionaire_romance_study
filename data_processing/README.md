
---

# Automated Preprocessing for NLP Tasks

#  The overall purpose of this code is preprocessing a large dataset of books for further NLP tasks. The preprocessing includes lemmatizing the tokens, categorizing them based on their POS tags, removal of certain kinds of tokens (characters names), and saving them in separate text files.


## Libraries Used
- csv
- os
- re
- pathlib
- pandas
- spacy

## Functionality

The script defines two main functions:

1. `lemmatize_and_remove_names(path)`: This function takes a file path as input, reads the data from the CSV file at that location, filters and processes it in various ways, and then writes the resulting data back to a text file in a specific directory structure.

2. `process_all_texts(rootdir)`: This function takes a root directory path as input and applies the `lemmatize_and_remove_names()` function to all .tokens files found within that directory and its subdirectories.

## Usage

To use this script, simply import the functions and call `process_all_texts()` with the root directory containing the .tokens files as the argument.

```python
from your_script import process_all_texts

process_all_texts(".source/novels_splitted_with_bookNLP")
```

The script will then read in each .tokens file, process it, and output the result to a new text file in a directory structure under "/home/polina/PycharmProjects/romantic_stories/full_dataset/novels_splitted_with_bookNLP/novels_by_lemmas".

Please ensure that Spacy's English Language Model ('en_core_web_sm') is downloaded and available for use by the script. You can download it using the following command:

```bash
python -m spacy download en_core_web_sm
```

---

Please replace "your_script" in the usage example with the actual name of your script.
