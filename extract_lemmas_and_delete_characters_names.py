import csv
import os
import re
from pathlib import Path
import pandas as pd
import spacy

#This script is a great example of how Python and its libraries can be used to automate the preprocessing of a large set
# of documents for natural language processing tasks. The result of this script would be a set of text files ready to be
# used in subsequent NLP tasks, such as topic modeling, text classification, or sentiment analysis.

# Load the English Language Model of Spacy.
spacy_client = spacy.load('en_core_web_sm')

def lemmatize_and_remove_names(path):
    df_tokens = pd.read_csv(path, sep="\t", quoting=csv.QUOTE_NONE)
    tokens_all = df_tokens.loc[(df_tokens['fine_POS_tag'] != "PER") & (df_tokens['POS_tag'] != "PUNCT")]
    tokens_verb_noun = df_tokens.loc[(df_tokens['POS_tag'] == "VERB") | (df_tokens['POS_tag'] == "NOUN")]
    tokens_noun = df_tokens.loc[(df_tokens['POS_tag'] == "NOUN")]
    tokens_adj_noun = df_tokens.loc[(df_tokens['POS_tag'] == "ADJ") | (df_tokens['POS_tag'] == "NOUN")]

    data_variants = {"tokens_all": tokens_all, "tokens_verb_noun": tokens_verb_noun, "tokens_noun": tokens_noun, "tokens_adj_noun": tokens_adj_noun}

    lemmas = {}
    book_path = "/".join(str(path).split("/")[:-1])
    print(book_path)

    book_id = "".join(str(path).split("/")[-1:]).split('.')[0]
    # print(book_id)

    for data_variant_name, data_variant in data_variants.items():
        lemmas[data_variant_name] = data_variant["lemma"].tolist()
        lemmas[data_variant_name] = [str(value).lower() for value in lemmas[data_variant_name]]
        lemma_string = " ".join(lemmas[data_variant_name])
        lemmas[data_variant_name] = lemma_string.replace("--", " ")
        lemmas[data_variant_name] = re.sub(r'[^A-Za-z ]+', '', lemma_string)
        lemmas[data_variant_name] = re.sub('\s+', ' ', lemmas[data_variant_name])
        lemmas[data_variant_name] = lemmas[data_variant_name].split()
        lemmas[data_variant_name] = [word for word in lemmas[data_variant_name] if
                                     word not in spacy_client.Defaults.stop_words and "www" not in word and len(
                                         word) > 2]
        # Create directories if they do not exist
        base_dir = "/home/polina/PycharmProjects/romantic_stories/full_dataset/novels_splitted_with_bookNLP/novels_by_lemmas"
        full_novels_dir = os.path.join(base_dir, 'novels_by_chapters_lemmas')  # 'novels_by_chapters_lemmas/'full_novels_by_lemmas'
        variant_dir = os.path.join(full_novels_dir, data_variant_name)
        os.makedirs(variant_dir, exist_ok=True)

        # Save txt file
        filename = f"{book_id}_{data_variant_name}.txt"
        file_path = os.path.join(variant_dir, filename)
        with open(file_path, "w") as text_file:
            text_file.write(" ".join(lemmas[data_variant_name]))


def process_all_texts(rootdir):
    for path in Path(rootdir).iterdir():  # iterate though all subdirs in rootdir
        if path.is_dir():
            process_all_texts(path)  # call this function on the subdir
        if path.is_file() and Path(path).suffix == '.tokens':
            lemmatize_and_remove_names(path)


process_all_texts(f".source/novels_splitted_with_bookNLP")
