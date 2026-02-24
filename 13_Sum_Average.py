# Q13 - Sum and Average Calculator
# This program calculates sum, average, max and min from user input numbers.

try:
    count = int(input("How many numbers do you want to enter? "))

    numbers = []

    for i in range(count):
        num = float(input("Enter number: "))
        numbers.append(num)

    total = sum(numbers)
    average = total / count

    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Count cannot be zero.")