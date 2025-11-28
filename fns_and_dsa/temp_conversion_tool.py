# temp_conversion_tool.py

# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Conversion functions
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# User interaction
def main():
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Enter the unit (C/F): ").strip().upper()
        
        if unit == "C":
            print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
        elif unit == "F":
            print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
        else:
            print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")

if __name__ == "__main__":
    main()
