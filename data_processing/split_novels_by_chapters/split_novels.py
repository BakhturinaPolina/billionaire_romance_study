import re
import os
from pathlib import Path
import pathlib
import string
import json

rootdir = "/home/polina/PycharmProjects/romantic_stories/novels_to_split_polina"

list_of_all_titles = []
list_of_all_texts = []

def get_preprocessed_text_from_txt(rootdir):
    for path in Path(rootdir).iterdir():  # iterate though all subdirs in rootdir
        if path.is_dir():
            get_preprocessed_text_from_txt(path)  # call this function on the subdir
        if path.is_file():
            with open(path) as file:
                heads, tails = os.path.split(path)  # split the path to the last part and everything else
                author_names = tails
                list_of_all_titles.append(author_names)
                text = file.read()
                list_of_all_texts.append(text)

get_preprocessed_text_from_txt(rootdir)

cleaned_list_of_titles = [] # store titles without 'docs' substring

for title in list_of_all_titles:
    title = title.replace('.docx', '')
    title = title.replace('.txt', '')
    cleaned_list_of_titles.append(title)

full_dictionary_of_splitted_novels = {}

for i, one_title in enumerate(cleaned_list_of_titles):
    full_dictionary_of_splitted_novels[one_title] = list_of_all_texts[i]

# After splitting text by chapters, the structure of the 'dictionary_of_splitted_novels' will look as follows:
# {key(name_of_book): (inner_key) (name_of_book + 'chapter' + number_of_chapter): (value) chapter_of_book) }

# EXAMPLE: {
#   'Book Title 1': {
#     'Book Title 1 Chapter 1': 'Part 1',
#     'Book Title 1 Chapter 2': 'Part 2',
#     'Book Title 1 Chapter 3': 'Part 3'
#   },
#   'Book Title 2': {
#     'Book Title 2 Chapter 1': 'Part 1',
#     'Book Title 2 Chapter 2': 'Part 2'
#   }
# }

# Create a new dictionary with the same keys and split values
split_books_dictionary = {}

for title, text in full_dictionary_of_splitted_novels.items():
    split_text = text.split('=-')
    split_books_dictionary[title] = split_text

# Create a new nested dictionary with title keys and chapter keys
nested_books_dictionary = {}

for title, chapters in split_books_dictionary.items():
    # In the following line, we create a dictionary for the current book title:
    # - f'{title} Chapter {i + 1}': chapter_text creates a new key-value pair for each chapter in the book
    # - The key is created by combining the book title, the word 'Chapter', and the chapter number (i + 1)
    # - The value is the text of the chapter (chapter_text)
    # - The enumerate(chapters) function is used to get both the index (i) and the text (chapter_text) for each chapter in the list of chapters
    # - The dictionary comprehension iterates over all chapters in the chapters list and creates a key-value pair for each chapter
    nested_books_dictionary[title] = {f'{title} Chapter {i + 1}': chapter_text for i, chapter_text in
                                      enumerate(chapters)}

# Now, nested_books_dictionary has the desired structure!

# Specify the initial directory path
initial_path = "novels_splitted_polina"

# Save each chapter as a separate text file
for title, chapters in nested_books_dictionary.items():
    # Create a new directory for each book, replace spaces with underscores and remove any special characters
    directory_name = os.path.join(initial_path, f"{title}_splitted")
    os.makedirs(directory_name, exist_ok=True)  # Create the directory, don't raise error if it already exists

    for chapter_name, chapter_text in chapters.items():
        # Replace spaces with underscores and remove any special characters in the filename
        filename = f"{chapter_name}_splitted.txt"

        # # Remove all non-alphabetical characters from chapter_text
        # chapter_text = re.sub(r'[^a-zA-Z\s]', '', chapter_text)

        with open(os.path.join(directory_name, filename), 'w') as text_file:  # Use os.path.join to create the full file path
            text_file.write(chapter_text)

# Save the nested_books_dictionary as a JSON file
with open('nested_books_dictionary.json', 'w') as json_file:
    json.dump(nested_books_dictionary, json_file, indent=4)


