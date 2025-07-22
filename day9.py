def calculate_tip(bill_amount, tip_percentage):
    return (bill_amount * tip_percentage) / 100

def split_bill(total_bill, people_count):
    return total_bill / people_count

while True:
    print("\nWelcome to the Bill Splitter App!\n")

    bill_amount = float(input("Enter total bill amount: "))
    people_count = int(input("Enter number of people: "))
    tip_percent = int(input("Enter tip percentage (0/5/10/15/20): "))

    tip_amount = calculate_tip(bill_amount, tip_percent)
    total_with_tip = bill_amount + tip_amount
    per_person = split_bill(total_with_tip, people_count)

    print(f"\nTip Amount: ₹{tip_amount:.2f}")
    print(f"Total Bill (with Tip): ₹{total_with_tip:.2f}")
    print(f"Each person should pay: ₹{per_person:.2f}\n")

    again = input("Would you like to calculate another bill? (y/n): ").lower()
    if again != 'y':break