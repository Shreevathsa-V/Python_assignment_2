# Q15 - Prime Number Checker
# A prime number has exactly two factors: 1 and itself.

def is_prime(n):
    if n <= 1:
        return False

    # Checking divisibility up to square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


try:
    number = int(input("Enter a number: "))

    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

    # Checking prime numbers in a given range
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    print("Prime numbers in the range:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

except ValueError:
    print("Invalid input.")