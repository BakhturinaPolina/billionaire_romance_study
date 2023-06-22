import csv
import os
import re
from pathlib import Path
import pandas as pd
import spacy

#  The overall purpose of this code is preprocessing a large dataset of books for further NLP tasks.
#  The preprocessing includes lemmatizing the tokens, categorizing them based on their POS tags, removal of certain kinds of tokens
#  (characters names), and saving them in separate text files.

# Load the English Language Model of Spacy.
spacy_client = spacy.load('en_core_web_sm')

# Define the function lemmatize_and_remove_names with path as the argument
def lemmatize_and_remove_names(path):
    # Load CSV file into a pandas DataFrame
    df_tokens = pd.read_csv(path, sep="\t", quoting=csv.QUOTE_NONE)
    # Filter tokens based on their fine POS tags and POS tags
    # Select all tokens that are not proper names ("PER") or punctuation ("PUNCT")
    tokens_all = df_tokens.loc[(df_tokens['fine_POS_tag'] != "PER") & (df_tokens['POS_tag'] != "PUNCT")]
    tokens_verb_noun = df_tokens.loc[(df_tokens['POS_tag'] == "VERB") | (df_tokens['POS_tag'] == "NOUN")]
    tokens_noun = df_tokens.loc[(df_tokens['POS_tag'] == "NOUN")]
    tokens_adj_noun = df_tokens.loc[(df_tokens['POS_tag'] == "ADJ") | (df_tokens['POS_tag'] == "NOUN")]

    # Store the token variants in a dictionary
    data_variants = {"tokens_all": tokens_all, "tokens_verb_noun": tokens_verb_noun, "tokens_noun": tokens_noun, "tokens_adj_noun": tokens_adj_noun}

    # Initialize dictionary for lemmas
    lemmas = {}
    # Get path to the book
    book_path = "/".join(str(path).split("/")[:-1])
    print(book_path)

    # Get book id
    book_id = "".join(str(path).split("/")[-1:]).split('.')[0]

    # Iterate over each token variant
    for data_variant_name, data_variant in data_variants.items():
        # Convert lemmas to list
        lemmas[data_variant_name] = data_variant["lemma"].tolist()
        # Lowercase all lemmas
        lemmas[data_variant_name] = [str(value).lower() for value in lemmas[data_variant_name]]
        # Join lemmas into a string
        lemma_string = " ".join(lemmas[data_variant_name])
        # Replace double hyphen with space
        lemmas[data_variant_name] = lemma_string.replace("--", " ")
        # Remove non-alphabetic characters
        lemmas[data_variant_name] = re.sub(r'[^A-Za-z ]+', '', lemma_string)
        # Replace multiple spaces with a single space
        lemmas[data_variant_name] = re.sub('\s+', ' ', lemmas[data_variant_name])
        # Split the string into words
        lemmas[data_variant_name] = lemmas[data_variant_name].split()
        # Filter out stop words, words containing 'www', and words with length <= 2
        lemmas[data_variant_name] = [word for word in lemmas[data_variant_name] if
                                     word not in spacy_client.Defaults.stop_words and "www" not in word and len(
                                         word) > 2]
        # Define directory paths
        base_dir = "/home/polina/PycharmProjects/romantic_stories/full_dataset/novels_splitted_with_bookNLP/novels_by_lemmas"
        full_novels_dir = os.path.join(base_dir, 'novels_by_chapters_lemmas')
        variant_dir = os.path.join(full_novels_dir, data_variant_name)
        # Create directories if they don't exist
        os.makedirs(variant_dir, exist_ok=True)

        # Define filename and file path
        filename = f"{book_id}_{data_variant_name}.txt"
        file_path = os.path.join(variant_dir, filename)
        # Write lemmas to the text file
        with open(file_path, "w") as text_file:
            text_file.write(" ".join(lemmas[data_variant_name]))

# Define the function process_all_texts with rootdir as the argument
def process_all_texts(rootdir):
    # Iterate over all subdirectories and files in the root directory
    for path in Path(rootdir).iterdir():
        # If the path is a directory, call the function on the subdirectory
        if path.is_dir():
            process_all_texts(path)
        # If the path is a file with the extension '.tokens', apply the function lemmatize_and_remove_names on the file
        if path.is_file() and Path(path).suffix == '.tokens':
            lemmatize_and_remove_names(path)

# Call the function process_all_texts on the specified directory
process_all_texts(f"/home/polina/PycharmProjects/romantic_stories/full_dataset/novels_splitted_with_bookNLP")
