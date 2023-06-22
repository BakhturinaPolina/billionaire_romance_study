# BookNLP for Romantic Novels Processing

This repository contains a Python script for pre-processing a dataset of romantic novels using BookNLP and spaCy.

## Requirements

To run the script, you need to have installed:

- `booknlp`
- `spacy`
- `en_core_web_sm` language model for spaCy

You can install the necessary packages with the following commands:

```bash
pip install booknlp
python -m spacy download en_core_web_sm
```

## Usage

The script processes all text files in the specified directory and outputs the results to a corresponding directory in the same root. The outputs contain the processed data for each novel.

If you're running the script on Google Colaboratory, make sure to mount your Google Drive to the `/content/drive` directory in the Colab environment. Update the `rootdir` and `output_directory_base` variables to match your file paths.

The script uses the `en_core_web_sm` language model for processing. You can adjust the `model_params` variable to use different components of the BookNLP pipeline or change the model.

```python
model_params = {
    "pipeline": "entity,quote,supersense,event,coref",
    "model": "small"
}
```

The script comes with two predefined functions to process all texts:
- `process_all_texts()` which processes books split by chapters keeping the directory structure,
- `process_all_texts_full()` which processes the entire books.

Uncomment the function call at the end of the script that suits your dataset organization.

For further information about the code, refer to the inline comments in the script.

## Contribution

Your contributions are always welcome. If you find any bugs or have any suggestions, feel free to create an issue or make a pull request.
