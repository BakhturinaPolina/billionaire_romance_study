# the code allowing to analyze novels by chapters with LIWC

# moint colab with google drive first
from google.colab import drive
drive.mount('/content/drive')

# install the LIWC library
! pip install liwc

# import other necessary libraries
import liwc
import nltk
from nltk import word_tokenize
# this is the path to a LIWC dictionary which is necessary for the library to work properly, the 2007 version can be easily found on the internet for free
# dowmload it and put to the folder you are working with
liwc_path = '/content/drive/MyDrive/billionaire_romance_study/code/LIWC2007_English100131.dic'
parse, category_names = liwc.load_token_parser(liwc_path)
import json
import pandas as pd
import re

# get the paths to the files
# insert a root directory
# here it is a directory with toy novels without names of characters splitted by chapters
rootdir = '/content/drive/MyDrive/billionaire_romance_study/toy_dataset_splitted_with_names'
import os
directory = rootdir
file_paths = []

for root, _, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)
# to check how many paths to files were found
print(f'There are {len(file_paths)} paths found.')

# sort the paths by alphanumerical order
def alphanumeric_sort_key(element):
    # split the element into alphabetical and numeric parts
    parts = re.split(r'(\d+)', element)

    # convert numeric parts to integers for proper numeric comparison
    parts[1::2] = map(int, parts[1::2])

    return parts

# sort the paths
file_paths_sorted = sorted(file_paths, key=alphanumeric_sort_key)
# print the first five as an example
for file_path in file_paths_sorted[:5]:
  print(file_path)

# group the chapters by the books they belong to
book_chapters = {}

for file_path in file_paths_sorted:
    # extract the book name from the file path
    book_name = os.path.basename(os.path.dirname(file_path))

    # add the file path to the corresponding book's list of chapters
    if book_name in book_chapters:
        book_chapters[book_name].append(file_path)
    else:
        book_chapters[book_name] = [file_path]

# iterate over all the books and their chapters
for book, chapters in book_chapters.items():
    print("Book:", book)
    print("Chapters:", chapters)
    print()

# access the books' names and their chapters
book_names = list(book_chapters.keys())
len(book_names)
book = book_names[...] # insert the index of an element here
print(f'The book: {book_names[...]}.') # change here as well

# access the number of chapters for a specific book
num_chapters = len(book_chapters[book])
print(f'The book contains {num_chapters} chapters.')

# get the chapters' paths
chapters_for_book = book_chapters[book]

# create a list of chapters' texts
def get_chapters_texts(chapters_file_paths):
  list_of_texts = []
  for chapter_file_path in chapters_file_paths:
    text_file = open(chapter_file_path)
    text = text_file.read()
    list_of_texts.append(text)
    text_file.close()
  return list_of_texts

book_list_of_texts = get_chapters_texts(chapters_for_book)
print(f'There are {len(book_list_of_texts)} chapters in the list.')

# preprocess the book chapters
# tokenize with nltk
import re
import nltk
nltk.download('punkt')  # Downloads the tokenizer data
nltk.download('stopwords')  # Downloads stopwords data (optional)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def preprocess_text(text):
    # remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # convert text to lowercase
    text = text.lower()

    # tokenize the text
    tokens = word_tokenize(text)

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    stop_words.update('’')
    tokens = [token for token in tokens if token not in stop_words]

    return tokens

preprocessed_chapters = []
for chapter in book_list_of_texts:
  preprocessed_chapter = preprocess_text(chapter)
  preprocessed_chapters.append(preprocessed_chapter)

print(f'There are {len(preprocessed_chapters)} preprocessed chapters.')

# check the categories in each chapter with LIWC
from collections import Counter
list_of_categories_by_book = []
for chapter in preprocessed_chapters:
  recognized_categories = []
  chapter_counts =  Counter(category for token in chapter for category in parse(token))
  cat_dict = Counter.most_common(chapter_counts)
  recognized_categories.append(cat_dict)
  list_of_categories_by_book.append(recognized_categories)
print(len(list_of_categories_by_book))

# save the list of categories by chapter as a csv file
categories = {'liwc categories': list_of_categories_by_book}
df = pd.DataFrame(categories)
df.index = range(1, len(df) + 1)
df
df.to_csv('shen_villain_liwc.csv', index=False)

"""# LIWC categories in the whole toy dataset"""

# create a list of chapters' texts
def get_chapters_texts(chapters_file_paths):
  list_of_texts = []
  for chapter_file_path in chapters_file_paths:
    text_file = open(chapter_file_path)
    text = text_file.read()
    list_of_texts.append(text)
    text_file.close()
  return list_of_texts

texts = get_chapters_texts(file_paths_sorted)
print(len(texts))

# preprocess all the texts
# preprocess the book chapters
# tokenize with nltk
import re
import nltk
nltk.download('punkt')  # Downloads the tokenizer data
nltk.download('stopwords')  # Downloads stopwords data (optional)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Convert text to lowercase
    text = text.lower()

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    stop_words.update('’')
    tokens = [token for token in tokens if token not in stop_words]

    return tokens

preprocessed_texts = []
for text in texts:
  preprocessed_text = preprocess_text(text)
  preprocessed_texts.append(preprocessed_text)

print(f'There are {len(preprocessed_texts)} preprocessed texts from the toy dataset.')

# concatenate the lists to work on all the tokens at once
concatenated_list = []
for sublist in preprocessed_texts:
    concatenated_list.extend(sublist)

# identify the categories in the whole toy dataset
from collections import Counter
counts =  Counter(category for token in concatenated_list for category in parse(token))
cat_dict_all = Counter.most_common(counts)
print(f"LiWC has identified {len(cat_dict_all)} categories in the toy dataset.")
print()
print('The categories are...')
for item in cat_dict_all:
  print(item)

import pandas as pd

# Specify the path to your CSV file
csv_file = "/content/drive/MyDrive/billionaire_romance_study/code/liwc_categories.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file, error_bad_lines=False, sep = ';')
words_lists = []
for i, words in enumerate(df):
  words_item = df.iloc[:, i].to_list()
  words_lists.append(words_item)

# delete the last empty element
words_lists.pop()
len(words_lists)

# delete nan elements
words_lists = [[x for x in sublist if not pd.isna(x)] for sublist in words_lists]
print(len(words_lists))
for sublist in words_lists:
  print(sublist)

# delete asterstks with re
final_words_lists = []
for sublist in words_lists:
  final_sublist = []
  for word in sublist:
    if "*" in word:
      new_word = re.sub("\*", '', word)
      final_sublist.append(new_word)
    else:
      final_sublist.append(word)
  final_words_lists.append(final_sublist)

# zip categories' names and the words corresponding to them and create dictionaries for the further analysis
labels = ['relativ', 'cogmech', 'verb', 'affect', 'percept', 'bio', 'time', 'social', 'posemo', 'present']
words = final_words_lists
cat_dictionaries = [{label: sublist} for label, sublist in zip(labels, words)]

# Print the list of dictionaries
for dictionary in cat_dictionaries:
    print(dictionary)

# save the final dictioaries as a json file
import json
with open("cat_dictionaries.json", "w") as file:
    json.dump(cat_dictionaries, file)

import json
file_path = '/content/drive/MyDrive/billionaire_romance_study/code/cat_dictionaries.json'
with open(file_path) as file:
  cat_dictionaries = json.load(file)
for dictionary in cat_dictionaries:
  print(dictionary)

# define the function that return the corresponding words to a given category and a list of words
# insert the index of a category from a list of dictionaries
def get_matching_words(i, concatenated_list, file_name):
  # access the list of terms for a given category
  category = cat_dictionaries[i]
  category_terms = list(category.values())
  flattened_terms = category_terms[0]

  # find the matches in a list of tokens and a list of category's terms
  category_matches = [word for word in concatenated_list if word in flattened_terms]

  # count them
  category_matches_counts = {}

  for word in category_matches:
    if word in category_matches_counts:
        category_matches_counts[word] += 1
    else:
        category_matches_counts[word] = 1

  sorted_words = sorted(category_matches_counts, key=lambda x: category_matches_counts[x], reverse=True)
  for word in sorted_words:
    print(word, category_matches_counts[word])

  # save the output as a txt file
  with open(file_name, 'w') as file:
    for word in sorted_words:
        print(word, category_matches_counts[word], file=file)

# 'relativ', 'cogmech', 'verb', 'affect', 'percept', 'bio', 'time', 'social', 'posemo', 'present'
matches_sorted = get_matching_words(..., concatenated_list, '..._matches.txt') # insert an index of a categoty and its name to the title
matches_sorted
