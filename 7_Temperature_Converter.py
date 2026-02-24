# Q7 - Temperature Converter
# This program converts temperature between different units.

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

try:
    choice = int(input("Enter your choice: "))
    temperature = float(input("Enter temperature value: "))

    # Checking choice and applying appropriate formula
    if choice == 1:
        result = (temperature * 9/5) + 32
        print("Converted temperature:", result)

    elif choice == 2:
        result = (temperature - 32) * 5/9
        print("Converted temperature:", result)

    elif choice == 3:
        result = temperature + 273.15
        print("Converted temperature:", result)

    elif choice == 4:
        result = temperature - 273.15
        print("Converted temperature:", result)

    else:
        print("Invalid choice.")

except ValueError:
    print("Invalid input. Please enter numeric values.")