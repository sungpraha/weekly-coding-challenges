"""
FizzBuzz Problem
================
Simple and clean FizzBuzz implementation.
"""

def fizzbuzz(n=100):
    """
    Print numbers 1 to n, replacing multiples of 3 with 'Fizz',
    multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'.
    
    Args:
        n (int): The upper limit (inclusive) for FizzBuzz
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizzbuzz_list(n=100):
    """
    Return FizzBuzz results as a list (for testing).
    
    Args:
        n (int): The upper limit (inclusive) for FizzBuzz
        
    Returns:
        list: List of FizzBuzz results
    """
    results = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(i)
    return results


def test_fizzbuzz():
    """Test the FizzBuzz implementation."""
    print("Testing FizzBuzz...")
    
    # Test first 15 numbers
    results = fizzbuzz_list(15)
    expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
    
    print("Results: ", results)
    print("Expected:", expected)
    
    if results == expected:
        print("✅ Test passed!")
    else:
        print("❌ Test failed!")
    
    print()


def interactive_fizzbuzz():
    """Interactive version where user can specify the range."""
    print("=== Interactive FizzBuzz ===")
    
    try:
        n = int(input("Enter a number (1 to n): "))
        if n <= 0:
            print("Please enter a positive number!")
            return
        
        print(f"\nFizzBuzz from 1 to {n}:")
        fizzbuzz(n)
        
    except ValueError:
        print("Please enter a valid number!")


if __name__ == "__main__":
    # Run test
    test_fizzbuzz()
    
    # Run default FizzBuzz (1 to 100)
    print("FizzBuzz 1 to 100:")
    fizzbuzz(100)
    
    # Ask if user wants interactive version
    print("\n" + "="*30)
    choice = input("Try interactive version? (y/n): ").lower()
    if choice.startswith('y'):
        interactive_fizzbuzz()