# Q8 - Leap Year Checker
# A leap year is divisible by 4 but not by 100,
# unless it is also divisible by 400.

try:
    year = int(input("Enter a year: "))

    # Applying leap year rule
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is NOT a Leap Year")

except ValueError:
    print("Please enter a valid year.")