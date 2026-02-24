# Q18 - Calculator using Functions
# Each operation is implemented using separate functions.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Power 7.Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 7:
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(add(num1, num2))
        elif choice == 2:
            print(subtract(num1, num2))
        elif choice == 3:
            print(multiply(num1, num2))
        elif choice == 4:
            print(divide(num1, num2))
        elif choice == 5:
            print(modulus(num1, num2))
        elif choice == 6:
            print(power(num1, num2))
        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input.")