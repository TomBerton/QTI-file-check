import os
import re

def find_incorrectly_formatted_questions(file_path):
    """Identify incorrectly formatted questions in a text file."""
    # Extract and print only the file name
    file_name = os.path.basename(file_path)
    print(f"\nTesting file: {file_name}")

    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into individual questions using question numbering (e.g., "1.", "2.", etc.)
    questions = re.split(r'\n(?=\d+\.)', content)

    # Define regex pattern to check for "*", "[*]" preceding "... Explanation:"
    incorrect_format_pattern = re.compile(r'\.\.\. Explanation:')

    # Identify questions that match the incorrect format
    incorrect_format = []
    for question in questions:
        if incorrect_format_pattern.search(question):
            # Get the line with "... Explanation:"
            explanation_line_index = next(
                (i for i, line in enumerate(question.splitlines()) if "... Explanation:" in line), None
            )

            # Check if the preceding line starts with "*" or "[*]"
            if explanation_line_index is not None:
                lines = question.splitlines()
                if explanation_line_index == 0 or not (
                    lines[explanation_line_index - 1].strip().startswith('*') or
                    lines[explanation_line_index - 1].strip().startswith('[*]')
                ):
                    incorrect_format.append(question.strip())

    # Display results
    if incorrect_format:
        print("Questions with incorrect format:")
        for question in incorrect_format:
            print("\n" + question)
    else:
        print("All questions are correctly formatted.")
