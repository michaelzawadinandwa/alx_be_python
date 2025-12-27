def main():
	print("Simple Match-Case Calculator")

	# Read first number using the exact prompt expected by tests
	s1 = input("Enter the first number:")
	# parse number: prefer int when possible
	try:
		if "." in s1:
			num1 = float(s1)
		else:
			num1 = int(s1)
	except ValueError:
		print("Invalid number. Please enter a valid number (e.g. 3, 4.5).")
		return

	# Read second number using the exact prompt expected by tests
	s2 = input("Enter the second number:")
	try:
		if "." in s2:
			num2 = float(s2)
		else:
			num2 = int(s2)
	except ValueError:
		print("Invalid number. Please enter a valid number (e.g. 3, 4.5).")
		return

	# Operation prompt
	operation = input("Choose the operation (+, -, *, /):").strip()

	match operation:
		case "+":
			result = num1 + num2
		case "-":
			result = num1 - num2
		case "*":
			result = num1 * num2
		case "/":
			if num2 == 0:
				print("Error: Cannot divide by zero.")
				return
			result = num1 / num2
		case _:
			print(f"Unknown operation: {operation!r}. Choose one of +, -, *, /. ")
			return

	# Output the result in the format expected by tests
	print(f"The result is {result}")


if __name__ == "__main__":
	main()

