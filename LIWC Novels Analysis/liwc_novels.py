'''The code below takes a list of preprocessed chapters (cleaned, lowered, tokenized, stopwords removed) for a book as input and
returns a list of found LIWC categories with the number of words for each category. It analyzes each token in each list element
and assigns it to one or more LIWC categories if it is found in the dictionary. 
The code is adjusted to work in the Colab environment.'''

# install the LIWC library
! pip install liwc

# import other necessary libraries
import liwc
# this is the path to a LIWC dictionary which is necessary for the library to work properly, the 2007 version can be easily found on the internet for free
# dowmload it and put in the folder you are working with
liwc_path = '/content/drive/MyDrive/billionaire_romance_study/code/LIWC2007_English100131.dic'
parse, category_names = liwc.load_token_parser(liwc_path)

# to save the outputs as separate csv files
import pandas as pd 

# cleaning
import re

# check the categories in each chapter with LIWC
from collections import Counter
list_of_categories_by_book = []
for chapter in preprocessed_chapters:
  recognized_categories = []
  chapter_counts =  Counter(category for token in chapter for category in parse(token))
  cat_dict = Counter.most_common(chapter_counts)
  recognized_categories.append(cat_dict)
  list_of_categories_by_book.append(recognized_categories)
# print out the number of LIWC categories found for a given book
print(len(list_of_categories_by_book))

# save the list of categories by chapter as a csv file
categories = {'liwc categories': list_of_categories_by_book}
df = pd.DataFrame(categories)
df.index = range(1, len(df) + 1)
df
df.to_csv('***.csv', index=False) # insert the name of a file

'''The code below allows to extract LIWC categories from the whole dataset.
The list of preprocessed chapters is first concatenated and then all the tokens are analyzed altogether.'''
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

# specify the path to your csv file
# this is csv a file containing words and stems for the first 10 most frequent LIWC categories
csv_file = ".../liwc_categories.csv"

# to work with the file, it has to be modified into a dictionary, where keys are LIWC category names and values are the words corresponding to them
# the following code allows to implement all the necessary steps
# read the csv file as a df
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

# delete asterisks with re
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
# 10 most frequent categories 
labels = ['relativ', 'cogmech', 'verb', 'affect', 'percept', 'bio', 'time', 'social', 'posemo', 'present'] 
words = final_words_lists
cat_dictionaries = [{label: sublist} for label, sublist in zip(labels, words)]

# print the list of dictionaries
for dictionary in cat_dictionaries:
    print(dictionary)

# save the final dictionaries as a json file
import json
with open("cat_dictionaries.json", "w") as file:
    json.dump(cat_dictionaries, file)

import json
file_path = '.../cat_dictionaries.json'
with open(file_path) as file:
  cat_dictionaries = json.load(file)
for dictionary in cat_dictionaries:
  print(dictionary)

# define the function that returns the corresponding words to a given category and a list of words
# insert the index of a category from a list of dictionaries
def get_matching_words(i, concatenated_list, file_name):
  # access the list of terms for a given category [i]
  category = cat_dictionaries[i]
  category_terms = list(category.values())
  flattened_terms = category_terms[0]

  # find the matches in a list of tokens and a list of the category's terms
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
matches_sorted = get_matching_words(..., concatenated_list, '***_matches.txt') # insert an index of a categoty and its name to the title
# all the matches found from the most to the least frequent terms
matches_sorted
