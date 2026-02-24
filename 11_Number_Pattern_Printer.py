# Q11 - Number Pattern Printer
# This program prints different number patterns based on user choice.

try:
    height = int(input("Enter the height of the pattern: "))
    
    print("Choose pattern type:")
    print("1. Increasing numbers")
    print("2. Repeated row numbers")
    print("3. Reverse decreasing pattern")
    print("4. Pyramid pattern")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Pattern: 1
        #          1 2
        #          1 2 3
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif choice == 2:
        # Pattern: 1
        #          2 2
        #          3 3 3
        for i in range(1, height + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    elif choice == 3:
        # Reverse decreasing pattern
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    elif choice == 4:
        # Pyramid pattern like 1, 121, 12321
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    else:
        print("Invalid choice.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")