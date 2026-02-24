# Q5 - Bill Splitter
# This program calculates tax, tip and splits the total amount among people.

try:
    # Taking inputs
    total_bill = float(input("Enter total bill amount: "))
    number_of_people = int(input("Enter number of people: "))
    tax_percentage = float(input("Enter tax percentage: "))
    tip_percentage = float(input("Enter tip percentage: "))

    # Calculating tax amount
    tax_amount = total_bill * tax_percentage / 100

    # Adding tax to original bill
    bill_after_tax = total_bill + tax_amount

    # Calculating tip on taxed amount
    tip_amount = bill_after_tax * tip_percentage / 100

    # Final total bill
    final_total = bill_after_tax + tip_amount

    # Splitting per person
    per_person_amount = final_total / number_of_people

    # Displaying results
    print("\nBill Summary")
    print("Subtotal:", total_bill)
    print("Tax amount:", tax_amount)
    print("Bill after tax:", bill_after_tax)
    print("Tip amount:", tip_amount)
    print("Total bill:", final_total)
    print("Amount per person:", per_person_amount)

except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Number of people cannot be zero.")