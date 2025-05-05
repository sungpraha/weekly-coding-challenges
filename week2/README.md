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
