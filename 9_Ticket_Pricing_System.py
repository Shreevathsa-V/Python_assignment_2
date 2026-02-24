# Q9 - Ticket Pricing System
# This program calculates ticket price based on age and day discount.

try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").lower()
    ticket_count = int(input("Enter number of tickets: "))

    # Determining base price based on age
    if age < 3:
        base_price = 0
    elif 3 <= age <= 12:
        base_price = 150
    elif 13 <= age <= 59:
        base_price = 300
    else:
        base_price = 200

    # Checking if weekend discount applies
    if day in ["friday", "saturday", "sunday"]:
        discount = base_price * 0.20
    else:
        discount = 0

    final_price_per_ticket = base_price - discount
    total_amount = final_price_per_ticket * ticket_count

    # Output
    print("Price per ticket:", final_price_per_ticket)
    print("Total amount:", total_amount)

except ValueError:
    print("Invalid input.")