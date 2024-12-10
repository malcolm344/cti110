# Malcolm Wiliams
# 11/14/2024
# P1HW2
# This program calculates and displays
# Travel Expenses based on user input.

print("This program calculates and displays travel expenses.\n")
budget = int(input("Enter Budget: "))
location = input("\nEnter your travel destination: ")
gas = int(input("\nHow much do you think you will spend on gas? "))
hotel = int (input("\nApproximately, how much will you need for accomodation/hotel? "))
food = int(input("\nLast, how much do you need for food? "))



#calc expenses
expenses = gas +hotel+ food
# Calc balance
remainAmount = budget - expenses

#display results
print("\n---------Travel Expenses---------")
print("location:",location)
print("Intitial Budget: " ,budget)
print("\nFuel:" ,gas)
print("Accomodation:",hotel)
print("Food:",food)

print("\nRemaining Balance:",remainAmount)

 
