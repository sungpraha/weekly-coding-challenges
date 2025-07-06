# week2/reverse_vowels.py

from typing import List # Although List isn't strictly needed here, it's good practice if you used it elsewhere or might expand

def reverseVowels(s: str) -> str:
    """
    Reverses the vowels in a string s, keeping non-vowels in place.
    Vowels are a, e, i, o, u (case-insensitive).
    """
    s_list = list(s)
    vowels = set('aeiouAEIOU')
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer until it points to a vowel or meets right
        while left < right and s_list[left] not in vowels:
            left += 1
        # Move right pointer until it points to a vowel or meets left
        while left < right and s_list[right] not in vowels:
            right -= 1

        # If pointers haven't crossed, swap the vowels
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]

        # Move pointers inward for the next iteration
        left += 1
        right -= 1

    return ''.join(s_list)

# --- Testing ---
if __name__ == "__main__":
    print("Running tests for reverseVowels...")
    assert reverseVowels("hello") == "holle", "Test Case 1 Failed: hello"
    assert reverseVowels("leetcode") == "leotcede", "Test Case 2 Failed: leetcode"
    assert reverseVowels("aA") == "Aa", "Test Case 3 Failed: aA"
    assert reverseVowels("bcdfg") == "bcdfg", "Test Case 4 Failed: bcdfg"
    assert reverseVowels("aeiou") == "uoiea", "Test Case 5 Failed: aeiou"
    assert reverseVowels(" ") == " ", "Test Case 6 Failed: space"
    assert reverseVowels("Uber") == "ebUr", "Test Case 7 Failed: Uber"
    print("All test cases passed!")