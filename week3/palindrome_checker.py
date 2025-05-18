def is_palindrome_simple(text):
    """
    Checks if a string is a palindrome (simple version).
    This version is case-sensitive and considers spaces.
    """
    # Reverse the string
    reversed_text = text[::-1]
    # Check if the original string is the same as the reversed one
    return text == reversed_text

def is_palindrome_advanced(text):
    """
    Checks if a string is a palindrome, ignoring spaces, punctuation, and case.
    """
    # 1. Normalize the string:
    #    a. Convert to lowercase
    #    b. Remove non-alphanumeric characters (spaces, punctuation)
    normalized_text = ""
    for char in text:
        if char.isalnum(): # Check if the character is alphanumeric (letter or number)
            normalized_text += char.lower()

    # 2. Check if the normalized string is a palindrome
    reversed_text = normalized_text[::-1]
    return normalized_text == reversed_text

# --- Example Usage ---
print("--- Simple Palindrome Checker ---")
print(f"'madam': {is_palindrome_simple('madam')}")        # Expected: True
print(f"'racecar': {is_palindrome_simple('racecar')}")      # Expected: True
print(f"'hello': {is_palindrome_simple('hello')}")        # Expected: False
print(f"'Madam': {is_palindrome_simple('Madam')}")        # Expected: False (due to case sensitivity)
print(f"'nurses run': {is_palindrome_simple('nurses run')}") # Expected: False (due to space)

print("\n--- Advanced Palindrome Checker ---")
print(f"'madam': {is_palindrome_advanced('madam')}")                 # Expected: True
print(f"'Racecar': {is_palindrome_advanced('Racecar')}")             # Expected: True
print(f"'A man, a plan, a canal: Panama': {is_palindrome_advanced('A man, a plan, a canal: Panama')}") # Expected: True
print(f"'Was it a car or a cat I saw?': {is_palindrome_advanced('Was it a car or a cat I saw?')}")   # Expected: True
print(f"'No 'x' in Nixon': {is_palindrome_advanced("No 'x' in Nixon")}") # Expected: True
print(f"'hello world': {is_palindrome_advanced('hello world')}")       # Expected: False