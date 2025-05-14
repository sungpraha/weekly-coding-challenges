# prime_checker.py
import math # Will be used for the square root optimization

def is_prime(number):
    """
    Checks if a given integer is a prime number.

    Args:
        number: An integer.

    Returns:
        True if the number is prime, False otherwise.
    """
    # --- Handle Edge Cases ---
    # Prime numbers are defined as natural numbers greater than 1.
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime.

    # 2 is the only even prime number.
    if number == 2:
        return True   # 2 is prime.

    # All other even numbers (greater than 2) are not prime.
    if number % 2 == 0:
        return False  # Even numbers (other than 2) are not prime.

    # --- Efficient Trial Division for Odd Numbers ---
    # If a number 'n' is not prime, it must have a factor less than or equal to its square root.
    # We only need to check for odd factors from 3 up to sqrt(number).
    # The upper limit for the range is int(math.sqrt(number)) + 1 to ensure the square root itself is included if it's an integer.
    # We step by 2 to only check odd divisors.
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            # If 'number' is divisible by any 'i' in this range, it's not prime.
            return False

    # If the loop completes without finding any factors, the number is prime.
    return True

# --- Example Usage (for testing) ---
if __name__ == "__main__":
    test_numbers = [-5, 0, 1, 2, 3, 4, 17, 25, 29, 997]
    for num in test_numbers:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")