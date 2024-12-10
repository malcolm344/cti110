# Malcolm Williams
# 1232024
# p2hw1
# Assignment assess student ability to edit and enhance exiting programs

budget = float(input("Enter budget: "))
destination = input("Enter your travel destination: ")
fuel = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculating remaining balance
total_expenses = fuel + accommodation + food
remaining_balance = budget - total_expenses

# Displaying the results
print("\n--------Travel Expenses--------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${fuel:,.2f}")
print(f"{'Accommodation:':<20} ${accommodation:,.2f}")
print(f"{'Food:':<20} ${food:,.2f}")
print("--------------------------------------")
print(f"{'Remaining Balance:':<20} ${remaining_balance:,.2f}")
