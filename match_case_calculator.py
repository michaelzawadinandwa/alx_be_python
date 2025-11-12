answer= input("enter the first number ")
answer=input("enter the second number ")
operation=input("enter any operation +,-,*,/")
match operation:
    case "+":
        print(f"The sum is: {int(answer)+int(answer)}")
    case "-":
        print(f"The difference is: {int(answer)-int(answer)}")
    case "*":
        print(f"The product is: {int(answer)*int(answer)}")
    case "/":
        if int(answer) != 0:
            print(f"The quotient is: {int(answer)/int(answer)}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter one of +, -, *, /.")
