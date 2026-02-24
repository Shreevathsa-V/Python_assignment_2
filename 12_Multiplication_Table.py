# Q12 - Multiplication Table Generator
# This program prints multiplication table for a given number.

try:
    number = int(input("Enter a number: "))
    limit = int(input("Enter the limit: "))

    for i in range(1, limit + 1):
        # Multiplying number with loop counter
        result = number * i
        print(number, "x", i, "=", result)

except ValueError:
    print("Invalid input. Please enter integers.")