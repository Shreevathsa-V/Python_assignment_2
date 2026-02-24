# Q2 - Simple Calculator
# This program performs basic arithmetic operations.

try:
    # Taking numeric input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Performing operations
    print("\nAddition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    # Division should not allow division by zero
    if num2 != 0:
        print("Division:", num1 / num2)
        print("Modulus:", num1 % num2)
    else:
        print("Division and modulus not possible (division by zero)")

    print("Power:", num1 ** num2)

except ValueError:
    # Handles cases where input is not numeric
    print("Invalid input. Please enter numbers only.")