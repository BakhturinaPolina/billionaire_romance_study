# -*- coding: utf-8 -*-
"""sentiment_analysis_novels.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19K5xFBSNklgFGEbuvRqJCZMgtkl22HqH

# 1. Prepare the dataset
"""

from google.colab import drive
drive.mount('/content/drive')

! pip install spacy

# libraries
import json
import pandas as pd
import re
import spacy
# load the model for nlp
nlp = spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS

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

# ---> the first 5 chapters

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

# access the books's names and their chapters
book_names = list(book_chapters.keys())
len(book_names)
book = book_names[...] # insert the index of an element here
print(f'The book: {book_names[...]}.') # change here as well

# access the number of chapters for a specific book
num_chapters = len(book_chapters[book])
print(f'The book contains {num_chapters} chapters')

# get the chapters' paths
chapters_for_book = book_chapters[book]
chapters_for_book

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

# preprocess texts with spacy
def preprocess_texts(list_of_texts):
  preprocessed_texts = []
  for text in list_of_texts:
    # remove non-alphabetical characters
    text = re.sub('\n', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize the text
    doc = nlp(text)

    # Remove stopwords and lemmatize
    lemmas = [token.lemma_.lower() for token in doc if not token.is_stop and len(token.text) > 2]

    # Return the preprocessed text as a string
    preprocessed_text = ' '.join(lemmas)
    preprocessed_text = re.sub(' +', ' ', preprocessed_text)
    preprocessed_texts.append(preprocessed_text)
  return preprocessed_texts

book_preprocessed_texts = preprocess_texts(book_list_of_texts)
print(f'There are {len(book_preprocessed_texts)} preprocessed chapters in the list.')

"""Now, when all the chapters are cleaned and preprocessed, it is time to extract the sentiments! First, let's check if the Pollyanna effect is present in a given book.

# 2. Pollyanna effect
## 2.1. Frequency of positive and negative words
"""

# for sentiment analysis
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def analyze_sentiments(text):
    sid = SentimentIntensityAnalyzer()
    positive_words = []
    negative_words = []

    for word in text.split():
        sentiment_scores = sid.polarity_scores(word)
        if sentiment_scores['compound'] > 0.5:
            positive_words.append(word)
        elif sentiment_scores['compound'] < -0.5:
            negative_words.append(word)

    return positive_words, negative_words

# analyze sentiments in each chapter
positive_all_by_chapters = []
negative_all_by_chapters = []

for text in book_preprocessed_texts:
  positive, negative = analyze_sentiments(text)
  positive_all_by_chapters.append(positive)
  negative_all_by_chapters.append(negative)
print(len(positive_all_by_chapters))
print(len(negative_all_by_chapters))

# count the number by positive and negative terms to confirm or reject the Polllyanna's hypothesis
positive_total = 0
negative_total = 0
n_pos = []
n_neg = []

for sublist in positive_all_by_chapters:
  n_pos.append(len(sublist))
  for word in sublist:
    positive_total += 1

for sublist in negative_all_by_chapters:
  n_neg.append(len(sublist))
  for word in sublist:
    negative_total += 1

print(f'Positive sentiments found: {positive_total}')
print(f'Negative sentiments found: {negative_total}')

# confirm of reject the presence of the effect in a given book
if positive_total > negative_total:
  print('Pollyanna effect confirmed!')
else:
  print('Pollyanna effect rejected :(')

# make a dfs with all positive and negative words by chapters
sentiments = {'Positive words': positive_all_by_chapters,
              'Positive words N': n_pos,
              'Negative words': negative_all_by_chapters,
              "Negative words N": n_neg}
df = pd.DataFrame(sentiments)
df.index = range(1, len(df) + 1)
df
df.to_csv('shen_villain.csv', index=False)

# pollyanna effect bar charts
positive_terms = [675, 781, 867, 908, 1166, 1405, 1322, 676, 578, 1267, 728, 802, 958, 895, 311, 2121, 873, 642, 500, 688]
negative_terms = [553, 391, 745, 434, 804, 929, 1094, 479, 589, 1127, 615, 1244, 827, 816, 573, 2052, 491, 960,489, 673]

import matplotlib.pyplot as plt

# Generate x-axis labels for each document
books = ['{}'.format(i+1) for i in range(20)]

# Set the width of the bars
bar_width = 0.35

# Set the positions of the bars on the x-axis
r1 = range(20)
r2 = [x + bar_width for x in r1]

# Create the bar graph
plt.bar(r1, positive_terms, color='#C79FEF', width=bar_width, edgecolor='black', label='Positive Terms')
plt.bar(r2, negative_terms, color='#E6E6FA', width=bar_width, edgecolor='black', label='Negative Terms')

# Add labels, title, and legend
plt.xlabel('Book')
plt.ylabel('Terms Count')
plt.title('Distribution of Positive and Negative Terms')
plt.xticks([r + bar_width/2 for r in range(20)], books)
plt.legend()

# Display the graph
plt.show()

# statistical analysis
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

positive_terms = np.array([675, 781, 867, 908, 1166, 1405, 1322, 676, 578, 1267, 728, 802, 958, 895, 311, 2121, 873, 642, 500, 688])
negative_terms = np.array([553, 391, 745, 434, 804, 929, 1094, 479, 589, 1127, 615, 1244, 827, 816, 573, 2052, 491, 960,489, 673])

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(positive_terms, negative_terms)

# Print the results
print("T-statistic:", round(t_statistic, 2))
print("P-value:", round(p_value, 2))

"""## 2.2. Diversity of positive and negative terms"""

import pandas as pd
import os
rootdir = '/content/drive/MyDrive/billionaire_romance_study/pollyanna_effect_dfs'
directory = rootdir
file_paths = []

for root, _, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)

print(f'There are {len(file_paths)} paths found.')

positive_terms = []
negative_terms = []

for file_path in file_paths:
    df = pd.read_csv(file_path)
    positive_terms.extend(df.iloc[:, 0].tolist())
    negative_terms.extend(df.iloc[:, 2].tolist())

positive_lists = []
negative_lists = []
for el in positive_terms:
  chapter_string = el.strip('[]')
  chapter_list = [word.strip().strip("'") for word in chapter_string.split(",")]
  positive_lists.append(chapter_list)

for el in negative_terms:
  chapter_string = el.strip('[]')
  chapter_list = [word.strip().strip("'") for word in chapter_string.split(",")]
  negative_lists.append(chapter_list)

pos_united_list = [word for sublist in positive_lists for word in sublist]
pos_united_list_final = list(filter(lambda elem: elem != '', pos_united_list))

neg_united_list = [word for sublist in negative_lists for word in sublist]
neg_united_list_final = list(filter(lambda elem: elem != '', neg_united_list))


print(f'The list of positive terms contains {len(pos_united_list_final)} entries.')
print(f'The list of negative terms contains {len(neg_united_list_final)} entries.')

# keep only unique entries
pos_unique_entries = list(set(pos_united_list_final))
print(f'There are {len(pos_unique_entries)} unique entries in the list of positive words.')

neg_unique_entries = list(set(neg_united_list_final))
print(f'There are {len(neg_unique_entries)} unique entries in the list of negative words.')

def count_unique_words(word_list):
    word_count = {}

    # count the occurrence of each word
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# positive words
word_counts_pos = count_unique_words(pos_united_list_final)
sorted_words_pos = sorted(word_counts_pos.items(), key=lambda x: x[1], reverse=True)
print('Positive words:')
for word, count in sorted_words_pos:
    print(word, ":", count)

print()
print()
print()

# negative words
word_counts_neg = count_unique_words(neg_united_list_final)
sorted_words_neg = sorted(word_counts_neg.items(), key=lambda x: x[1], reverse=True)
print('Negative words:')
for word, count in sorted_words_neg:
    print(word, ":", count)

"""# 3. Vonnegut's basic plots"""

! pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
# split text by sentences
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# calculate mean compound score
import statistics

# for this part RAW TEXTS should be used
texts = book_list_of_texts

texts_by_sentences = []
for text in texts:
  sentences = sent_tokenize(text)
  texts_by_sentences.append(sentences)
print(len(texts_by_sentences))

# sentiments by sentences
all_sentences_compound_scores = []

for chapter in texts_by_sentences:
  for sentence in chapter:
    sentiment_score = analyzer.polarity_scores(sentence)
    compound_score = sentiment_score['compound']
    all_sentences_compound_scores.append(compound_score)

print(f'There are {len(all_sentences_compound_scores)} compound scores in the list.')
print()
# divide the compound scores into chunks of 250 sentences
chunk_size = 250
# create sublists
sublists = [all_sentences_compound_scores[i:i+chunk_size] for i in range(0, len(all_sentences_compound_scores), chunk_size)]
print(f'There are {len(sublists)} sublists with 250 sentences in each.')
print()

# calculate mean compound scores for each sublist
import statistics
mean_by_250 = []
for sublist in sublists:
  mean_compound_score_by_sublist = statistics.mean(sublist)
  mean_by_250.append(mean_compound_score_by_sublist)
print(f'There are {len(mean_by_250)} mean compound scores for chunks 250 sentences each.')

import matplotlib.pyplot as plt

# prepare compound scores
x = range(len(mean_by_250))
y = mean_by_250

# create a wider figure
plt.figure(figsize=(32, 6))  # Adjust the width and height as needed

# create the line graph or bar graph
plt.plot(x, y, '.-', color='#C79FEF')
plt.fill_between(x, y, color='#E6E6FA', alpha=0.3)  # adjust color and transparency as desired

# add labels and title
plt.xlabel('Chunks by 250 sentences')
plt.ylabel('Compound scores')
plt.title('Compound scores by chunks "The Villain" by L. J. Shen')

# Set x-axis tick labels
tick_labels = list(map(str, range(1, len(mean_by_250) + 1)))
plt.xticks(range(len(mean_by_250)), tick_labels)

# Display the graph
plt.show()

# calculate mean compound scores by chapters
chapter_mean_compound_scores = []

for chapter in texts_by_sentences:
  sentences_compound_scores_by_chapter = []

  for sentence in chapter:
    sentiment_score = analyzer.polarity_scores(sentence)
    compound_score = sentiment_score['compound']
    sentences_compound_scores_by_chapter.append(compound_score)

  chapter_mean_compound_score = statistics.mean(sentences_compound_scores_by_chapter)
  chapter_mean_compound_scores.append(round(chapter_mean_compound_score, 3))

# print out the output
print(len(chapter_mean_compound_scores))
print(chapter_mean_compound_scores)

import matplotlib.pyplot as plt

# assuming chapter_mean_compound_scores is a list of scores
chapter_mean_compound_scores

# Create the x-axis values starting from 1
x_values = range(1, len(chapter_mean_compound_scores) + 1)

plt.figure(figsize=(28, 6))
# Create the plot
plt.plot(x_values, chapter_mean_compound_scores, '.-', color='#C79FEF')

# Fill the space under the line with a color
plt.fill_between(x_values, chapter_mean_compound_scores, color='#E6E6FA', alpha=0.3)

# Set labels and title
plt.xlabel('Chapter')
plt.ylabel('Compound score')
plt.title('Compound scores by chapters for "The Villain" by L. J. Shen')

# Customize the tick labels to show the chapter numbers
x_tick_labels = [str(x) for x in x_values]
plt.xticks(x_values, x_tick_labels)

# Show the plot
plt.show()