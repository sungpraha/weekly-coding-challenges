# week5/even_filter.py

def get_even_numbers(input_list):
    """
    Takes a list of integers and returns a new list
    containing only the even numbers from the original list.
    """
    even_numbers_list = []  # Initialize an empty list to store even numbers
    for number in input_list:
        if number % 2 == 0:  # Check if the number is even
            even_numbers_list.append(number)  # Add it to our list
    return even_numbers_list

# --- Example Usage ---
original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -2, -5]
filtered_evens = get_even_numbers(original_numbers)

print(f"Original list: {original_numbers}")
print(f"Even numbers list: {filtered_evens}")
