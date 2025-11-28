# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temp_input = input("Enter the temperature to convert: ")

    # Check for numeric temperature
    try:
        temperature = float(temp_input)
    except:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit.upper() == "F":
        result = convert_to_celsius(temperature)
        print(str(temperature) + "°F is " + str(result) + "°C")

    elif unit.upper() == "C":
        result = convert_to_fahrenheit(temperature)
        print(str(temperature) + "°C is " + str(result) + "°F")

    else:
        raise ValueError("Invalid unit. Please enter C or F.")


if __name__ == "__main__":
    main()
