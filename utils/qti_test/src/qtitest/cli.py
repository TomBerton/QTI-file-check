import os
import fire
import questionary
from qtitest.qti_testing import find_incorrectly_formatted_questions

def test():
    """The script tests all .txt files in the specified directory."""
    # Prompt the user for the directory path
    directory_path = input("Enter the directory path to check text files: ")

    # Validate the directory path
    if not os.path.isdir(directory_path):
        print("Invalid directory path. Please try again.")
        return

    # Get all text files in the directory
    text_files = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith('.txt')]

    if not text_files:
        print("No text files found in the directory.")
        return

    # Process each text file
    for file_path in text_files:
        print(f"\nChecking file: {file_path}")
        find_incorrectly_formatted_questions(file_path)

def cli():
    fire.Fire({
         "test": test
        })
