# Q4 - Age Calculator
# This program calculates age and related time values.

from datetime import datetime

try:
    birth_year = int(input("Enter your birth year: "))

    # Getting current year from system
    current_year = datetime.now().year

    age = current_year - birth_year

    print("\nCurrent age:", age)
    print("Age in months:", age * 12)
    print("Age in days (approx):", age * 365)
    print("Age in hours (approx):", age * 365 * 24)
    print("Age in minutes (approx):", age * 365 * 24 * 60)
    print("Years remaining to 100:", 100 - age)

except ValueError:
    print("Please enter a valid year.")