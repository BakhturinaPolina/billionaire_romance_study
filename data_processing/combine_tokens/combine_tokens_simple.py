import os
from pathlib import Path

tokens = {"tokens_all": "", "tokens_noun": "", "tokens_verb_noun": "", "tokens_adj_noun": ""}

def combine_tokens(rootdir):
    for path in Path(rootdir).iterdir():  # iterate though all subdirs in rootdir
        if path.is_dir():
            combine_tokens(path)  # call this function on the subdir
        if path.is_file() and Path(path).suffix == '.txt':
            with open(path) as f:
                contents = f.read()
                tokens[str(path).split("/")[-1].split(".")[-2]] += f" {contents}"


rootdir = '/home/polina/PycharmProjects/romantic_stories/full_dataset_for_LDA_output'  # Update with the correct root directory path
combine_tokens(rootdir)

for tokens_name, tokens_content in tokens.items():
    with open(f'/home/polina/PycharmProjects/romantic_stories/full_dataset_for_LDA_output/{tokens_name}.txt', 'w') as f:
        f.write(tokens_content)
