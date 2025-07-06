import string
from collections import Counter
import os # Optional: for more robust file path handling

def get_top_n_words(filepath: str, n: int) -> list:
    """
    Reads a text file, processes the text to count word frequencies,
    and returns the top N most frequent words.
    Hyphenated words are split into separate words (e.g., "well-being" -> "well", "being").
    Punctuation is removed, and words are treated case-insensitively.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Specifically handle hyphens: replace with space to split words
    text = text.replace('-', ' ')

    # 3. Remove other punctuation
    # Create a translation table that maps each punctuation character to None (to delete it)
    # We ensure hyphen is not in the string.punctuation set being removed if it was there,
    # or rely on it being replaced by a space already.
    # string.punctuation typically includes '-'
    # So, by replacing '-' with ' ' first, the translate step won't affect our split.
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # 4. Split into words (now "well being" will split into "well", "being")
    words = text.split()

    # 5. Optional: Filter out any empty strings that might have resulted from processing,
    # though text.split() is usually good at handling multiple spaces.
    words = [word for word in words if word]

    # 6. Count word frequencies
    if not words:
        return [] # No words to count
    word_counts = Counter(words)

    # 7. Get the top N most common words
    top_n = word_counts.most_common(n)

    return top_n

if __name__ == "__main__":
    # Construct the path to the text file relative to this script's location
    # This makes the script runnable from any directory, as long as the .txt file
    # is in the same directory as the .py file.
    try:
        current_script_directory = os.path.dirname(__file__)
        filepath = os.path.join(current_script_directory, "great_gatsby.txt")
    except NameError: 
        # __file__ is not defined if running in some interactive environments
        # Fallback to assuming the file is in the current working directory
        # or specifically where the user has placed it ('week2')
        filepath = "great_gatsby.txt" # If you run `python gatsby_top_words.py` from within 'week2'

    num_top_words = 10  # You can change this value

    print(f"Attempting to read from: {os.path.abspath(filepath)}") # Shows full path being tried

    top_words_found = get_top_n_words(filepath, num_top_words)

    if top_words_found:
        print(f"\nTop {num_top_words} most frequent words from '{filepath}':")
        for i, (word, count) in enumerate(top_words_found):
            print(f"{i+1}. {word}: {count}")