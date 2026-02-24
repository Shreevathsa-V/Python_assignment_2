# Q14 - Factorial Calculator
# Factorial of n means n × (n-1) × ... × 1

try:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")
    elif number == 0:
        print("0! = 1")
    else:
        factorial = 1

        # Loop from 1 to number
        for i in range(1, number + 1):
            factorial *= i

        print("Factorial of", number, "is", factorial)

except ValueError:
    print("Please enter a valid integer.")