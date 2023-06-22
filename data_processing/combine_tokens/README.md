# Text File Token Aggregator

This Python script is designed to combine tokens from multiple text files located in a directory and its subdirectories. The tokens are categorized as `tokens_all`, `tokens_noun`, `tokens_verb_noun`, and `tokens_adj_noun`. After gathering all the tokens, the script saves them as separate `.txt` files in the root directory.

## Features
- Iterates through all subdirectories and text files in a given directory.
- Combines tokens from all text files according to their category.
- Saves the combined tokens of each category to a separate `.txt` file.

## How to Use

To use this script, follow these steps:

1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed. You can check this by typing `python --version` in your terminal/command prompt.
3. Open `script.py` in your Python editor of choice.
4. Set `rootdir` variable to the path of the directory containing the text files you wish to process.
5. Run the script. The processed files with combined tokens will be saved in the directory specified in the `rootdir` variable.

**NOTE**: The script assumes that each text file contains a type of token that matches one of the categories in the `tokens` dictionary. If your text files contain different categories, be sure to update the `tokens` dictionary accordingly.

---

Please, adjust this to match the actual functionality of your project and any other requirements or dependencies your project might have.
