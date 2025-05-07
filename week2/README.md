# Week 2: Reverse Vowels in a String

## Problem

Given a string `s`, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', 'u', and they can appear in both lower and upper cases, more than once. Non-vowel characters should stay in their original positions.

## Examples

1.  **Input:** `s = "hello"`
    **Output:** `"holle"`

2.  **Input:** `s = "leetcode"`
    **Output:** `"leotcede"`

3.  **Input:** `s = "aA"`
    **Output:** `"Aa"`

## Constraints

* `1 <= s.length <= 3 * 10^5`
* `s` consists of **printable ASCII characters**.

## Solution Approach: Two Pointers

The problem asks us to reverse vowels while keeping consonants in place. This suggests a **two-pointer** approach:

1.  **Convert to List:** Strings in Python are immutable. Convert the input string `s` into a list of characters (`s_list`) to allow in-place modification.
2.  **Vowel Set:** Create a set containing all vowels (both lowercase and uppercase) for efficient O(1) average time lookup. `vowels = set('aeiouAEIOU')`.
3.  **Initialize Pointers:** Set a `left` pointer to the start of the list (`0`) and a `right` pointer to the end of the list (`len(s) - 1`).
4.  **Iterate and Swap:**
    * Use a `while left < right` loop to ensure pointers don't cross.
    * Inside the loop, move the `left` pointer forward (`left += 1`) as long as `left < right` and the character `s_list[left]` is *not* a vowel.
    * Similarly, move the `right` pointer backward (`right -= 1`) as long as `left < right` and the character `s_list[right]` is *not* a vowel.
    * Once both pointers point to vowels (or the loop condition `left < right` breaks), swap the characters: `s_list[left], s_list[right] = s_list[right], s_list[left]`.
    * After the potential swap, move both pointers inward (`left += 1`, `right -= 1`) to continue searching for the next pair of vowels.
5.  **Join Back:** After the loop finishes, join the characters in `s_list` back into a single string using `''.join(s_list)` and return it.

## Complexity Analysis

* **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. Each pointer (`left` and `right`) traverses the list at most once. Checking if a character is in the vowel set takes $O(1)$ average time.
* **Space Complexity:** $O(n)$. We create a list `s_list` from the string, which requires space proportional to the string's length. The `vowels` set uses constant space $O(1)$ as its size is fixed.

## Code

```python
# week2/reverse_vowels.py
from typing import List

def reverseVowels(s: str) -> str:
    s_list = list(s)
    vowels = set('aeiouAEIOU')
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1
        if left < right: # Ensure pointers didn't cross while searching
            s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    return ''.join(s_list)

-----

## Problem 2: Top N Most Frequent Words from "The Great Gatsby" Excerpt

**Date Added:** May 7, 2025

### Problem Description

The goal is to write a Python program that reads the content of `great_gatsby.txt`, processes the text to identify word frequencies, and then outputs the **N** most common words.

**Key text processing requirements include:**
* Case-insensitivity: "The" and "the" should be counted as the same word.
* Hyphenation: Hyphenated terms like "well-being" must be treated as two separate words: "well" and "being".
* Punctuation: Standard punctuation marks (periods, commas, quotes, etc.) should be removed and not interfere with word identification.

### Input Files

1.  `great_gatsby.txt`: The text file containing the first ~150 lines of "The Great Gatsby". This file should be placed in the `week2` directory.
2.  `N`: An integer specifying how many of the most frequent words to display (e.g., N=10).

### Example Output

Top 10 most frequent words from '/Users/sungha/Documents/coding/weekly-coding-challenges/week2/great_gatsby.txt':

the: 100
a: 72
and: 60
of: 58
i: 54
in: 40
that: 36
to: 35
was: 34
my: 22

### Solution Approach

The Python script (`gatsby_top_words.py`) implements the following logic:
1.  **Read File:** Opens and reads the content from the specified filepath (`great_gatsby.txt`), ensuring `utf-8` encoding. Includes basic error handling for `FileNotFoundError`.
2.  **Normalize Text (Lowercase):** Converts the entire text content to lowercase to handle case-insensitivity.
3.  **Handle Hyphens:** Replaces all hyphen characters (`-`) with spaces (` `). This is done *before* general punctuation removal to ensure terms like "well-being" become "well being" and are then split into two distinct words.
4.  **Remove Punctuation:** Uses `str.maketrans()` and `text.translate()` with `string.punctuation` to remove all other standard punctuation marks.
5.  **Tokenize (Split Words):** Splits the cleaned text into a list of individual words using whitespace as the delimiter. Any resulting empty strings from the list of words are filtered out.
6.  **Count Frequencies:** Employs `collections.Counter` to efficiently count the occurrences of each word in the tokenized list.
7.  **Extract Top N:** Uses the `.most_common(N)` method of the `Counter` object to get the N words with the highest frequencies, already sorted in descending order of frequency.
8.  **Display Results:** Prints the top N words and their counts in a formatted manner.

### Code Snippet

*(The core logic from `gatsby_top_words.py`)*
```python
import string
from collections import Counter
import os # Optional: for more robust file path handling

def get_top_n_words(filepath: str, n: int) -> list:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        # (Error handling)
        return []
    # ... (other error handling)

    text = text.lower()
    text = text.replace('-', ' ') # Handle hyphens as word separators
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    words = text.split()
    words = [word for word in words if word] # Filter empty strings

    if not words:
        return []
    word_counts = Counter(words)
    top_n = word_counts.most_common(n)
    return top_n
    
Insights & Learnings
The order of text processing operations is crucial (e.g., handling hyphens before general punctuation removal based on string.punctuation).
collections.Counter is an extremely convenient and efficient tool for frequency counting tasks.
Initial word frequency outputs often highlight the prevalence of "stop words" (common articles, prepositions, etc.), suggesting a common next step in text analysis is stop word filtering to find more thematically relevant terms.
Robust file path handling (e.g., using os.path.join and os.path.dirname(__file__)) makes scripts more portable.
