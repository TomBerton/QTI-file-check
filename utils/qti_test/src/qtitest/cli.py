import os
import fire
import questionary
from qtitest.qti_testing import find_incorrectly_formatted_questions

def test():
    """The script tests all .txt files in the specified directory."""
    # Prompt the user for the file path
    file_path = input("Enter the directory path to the text file: ")
    find_incorrectly_formatted_questions(file_path)

def cli():
    fire.Fire({
         "test": test
        })
