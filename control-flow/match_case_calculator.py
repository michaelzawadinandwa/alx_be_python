#!/usr/bin/env python3
"""Simple calculator using Python's match-case statement.

Prompts the user for two numbers and an operation (+, -, *, /),
performs the calculation, and displays the result. Handles division
by zero and invalid input gracefully.
"""

def get_number(prompt: str):
	while True:
		s = input(prompt)
		try:
			# Accept integers or floats
			if "." in s:
				return float(s)
			return int(s)
		except ValueError:
			print("Invalid number. Please enter a valid number (e.g. 3, 4.5).")


def main():
	print("Simple Match-Case Calculator")
	num1 = get_number("Enter the first number: ")
	num2 = get_number("Enter the second number: ")
	op = input("Choose the operation (+, -, *, /): ").strip()

	match op:
		case "+":
			result = num1 + num2
			op_name = "addition"
		case "-":
			result = num1 - num2
			op_name = "subtraction"
		case "*":
			result = num1 * num2
			op_name = "multiplication"
		case "/":
			if num2 == 0:
				print("Error: Cannot divide by zero.")
				return
			result = num1 / num2
			op_name = "division"
		case _:
			print(f"Unknown operation: {op!r}. Choose one of +, -, *, /.")
			return

	print(f"The result of the {op_name} is {result}")


if __name__ == "__main__":
	main()

