# week6/validator.py

def is_valid_parentheses(s):
    """
    Checks if a string of parentheses is valid using a stack.

    Args:
        s: A string containing only '()[]{}'.

    Returns:
        True if the string is valid, False otherwise.
    """
    # A dictionary to hold the matching pairs of brackets.
    # The keys are the closing brackets, and values are the opening ones.
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # A list to use as our stack.
    stack = []

    # Iterate through each character in the input string.
    for char in s:
        # If the character is a closing bracket...
        if char in matching_bracket:
            # ...and the stack is not empty, and the top of the stack is the
            # corresponding opening bracket...
            # We use a placeholder '#' if the stack is empty to avoid an error
            # and ensure the comparison fails.
            top_element = stack.pop() if stack else '#'
            
            if matching_bracket[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack.
            stack.append(char)
            
    # At the end, if the stack is empty, all brackets were matched correctly.
    # If the stack is not empty, there are unclosed opening brackets.
    return not stack

# --- Example Usage ---
print(f"'()': {is_valid_parentheses('()')}")                 # Expected: True
print(f"'()[]{{}}': {is_valid_parentheses('()[]{}')}")         # Expected: True
print(f"'(]': {is_valid_parentheses('(]')}")                 # Expected: False
print(f"'([)]': {is_valid_parentheses('([)]')}")             # Expected: False
print(f"'{{[]}}': {is_valid_parentheses('{[]}')}")             # Expected: True
print(f"']': {is_valid_parentheses(']')}")                   # Expected: False
print(f"'(': {is_valid_parentheses('(')}")                   # Expected: False
print(f"Empty string '': {is_valid_parentheses('')}")      # Expected: True (no brackets, so valid)