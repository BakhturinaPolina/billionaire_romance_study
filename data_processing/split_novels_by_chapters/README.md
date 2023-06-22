# Text Processing and Organization Script: Split Novels by Chapters

This project includes a Python script for processing text files, specifically novels, from a directory. The script is designed to read text from each file, split the text into chapters, and then save each chapter as a separate text file. This results in an organized and easily navigable directory structure. The final structure of processed novels is also saved as a JSON file for easy lookup and reference.

## Features
- Iterates through all subdirectories and files in a given directory.
- Processes each text file and saves the title and content in lists.
- Splits each book text into chapters using the delimiter '=-'.
- Saves each chapter as a separate text file in a dedicated folder for each book.
- Stores a JSON file representing the nested dictionary structure of books and their chapters.

## Output Structure

The resulting structure of the `nested_books_dictionary` will look as follows:
```python
{
  'Book Title 1': {
    'Book Title 1 Chapter 1': 'Part 1',
    'Book Title 1 Chapter 2': 'Part 2',
    'Book Title 1 Chapter 3': 'Part 3'
  },
  'Book Title 2': {
    'Book Title 2 Chapter 1': 'Part 1',
    'Book Title 2 Chapter 2': 'Part 2'
  }
}
```

## How to Use

To use this script, follow these steps:

1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed. You can check this by typing `python --version` in your terminal/command prompt.
3. Open `script.py` in your Python editor of choice.
4. Set `rootdir` variable to the path of the directory containing the text files you wish to process.
5. Set `initial_path` variable to the path of the directory where you wish to save the processed files.
6. Run the script. The processed files will be saved in the directory specified in `initial_path`.

**NOTE**: The script assumes that chapters in each novel are separated by the string '=-'. If your text files use a different delimiter, be sure to update the `text.split('=-')` line to use the correct delimiter.

---

You may need to adjust this to match the actual functionality of your project and any other requirements or dependencies your project might have.
