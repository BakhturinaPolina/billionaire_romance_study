'''The code below allows to explore two literary phenomena, 
the Pollyanna hypothesis and Vonnegut's basic plots through the implementation of VADER sentiment analysis tool.
It takes a list of preprocessed texts of chapters (cleaned, lowered, tokenized, lemmatized, joint into one string per chapter.'''

# pollyanna effect
## frequency of positive and negative words

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
df.to_csv('***.csv', index=False) # insert the name of a file

# diversity of positive and negative terms

import pandas as pd
import os
rootdir = '.../pollyanna_effect_dfs' # the directory where all dfs for all the books are saved
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

# Vonnegut's basic plots
'''The code below calculates the mean compound scores per chapter and per chunk of 250 sentences through VADER.
It takes a list of RAW chapters as input.'''

! pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
# split text by sentences
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

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

# create a line graph
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
plt.title('Compound scores by chunks for *book title*')

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

# create a line graph
import matplotlib.pyplot as plt

# assuming chapter_mean_compound_scores is a list of scores
chapter_mean_compound_scores

# create the x-axis values starting from 1
x_values = range(1, len(chapter_mean_compound_scores) + 1)

plt.figure(figsize=(28, 6))
# create the plot
plt.plot(x_values, chapter_mean_compound_scores, '.-', color='#C79FEF')

# fill the space under the line with a color
plt.fill_between(x_values, chapter_mean_compound_scores, color='#E6E6FA', alpha=0.3)

# set labels and title
plt.xlabel('Chapter')
plt.ylabel('Compound score')
plt.title('Compound scores by chapters for "The Villain" by L. J. Shen')

# customize the tick labels to show the chapter numbers
x_tick_labels = [str(x) for x in x_values]
plt.xticks(x_values, x_tick_labels)

# show the plot
plt.show()
