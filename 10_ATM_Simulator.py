# Q10 - Simple ATM Simulator
# This program simulates ATM operations with minimum balance rule.

balance = 10000
minimum_balance = 500

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Simply show current balance
            print("Current Balance:", balance)

        elif choice == 2:
            deposit_amount = float(input("Enter deposit amount: "))
            
            if deposit_amount > 0:
                balance += deposit_amount
                print("Deposit successful.")
                print("Updated balance:", balance)
            else:
                print("Deposit amount must be positive.")

        elif choice == 3:
            withdraw_amount = float(input("Enter withdrawal amount: "))

            if withdraw_amount <= 0:
                print("Withdrawal amount must be positive.")
            elif balance - withdraw_amount < minimum_balance:
                # Ensuring 500 remains in account
                print("Cannot withdraw. Minimum balance of 500 required.")
            else:
                balance -= withdraw_amount
                print("Withdrawal successful.")
                print("Updated balance:", balance)

        elif choice == 4:
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")