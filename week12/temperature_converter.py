# Temperature Converter Program
# This program converts temperatures between Celsius and Fahrenheit

def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    return (fahrenheit - 32) * 5/9

def main():
    """Main function to run the temperature converter program"""
    # Display the program title and menu options
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    # Get user's choice
    choice = input("Enter choice (1 or 2): ")
    
    # Process the conversion based on user's choice
    if choice == '1':
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {round(result, 1)}°F")
    elif choice == '2':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {round(result, 1)}°C")
    else:
        # Handle invalid input
        print("Invalid choice. Please select 1 or 2.")

# Run the program only if this file is executed directly (not imported)
if __name__ == "__main__":
    main()