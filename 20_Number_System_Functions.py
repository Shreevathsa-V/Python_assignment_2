# Q20 - Number System Functions
# This program performs multiple mathematical operations using functions.

def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n):
    return int(str(n)[::-1])

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


while True:
    print("\n1.Factorial 2.Prime 3.Fibonacci 4.SumDigits")
    print("5.Reverse 6.Armstrong 7.GCD 8.LCM 9.Perfect 10.Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 10:
            break

        if choice in [1, 2, 3, 4, 5, 6, 9]:
            n = int(input("Enter number: "))

            if choice == 1:
                print(factorial(n))
            elif choice == 2:
                print(is_prime(n))
            elif choice == 3:
                print(fibonacci(n))
            elif choice == 4:
                print(sum_of_digits(n))
            elif choice == 5:
                print(reverse_number(n))
            elif choice == 6:
                print(is_armstrong(n))
            elif choice == 9:
                print(is_perfect(n))

        elif choice in [7, 8]:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if choice == 7:
                print(gcd(num1, num2))
            else:
                print(lcm(num1, num2))

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input.")