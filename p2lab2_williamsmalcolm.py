# Malcolm Williams
# 11/20/24
# p2lab2
# Assignment tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user
# Creating the dictionary
car_milage = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Printing the dictionary to verify


# Creating a variable that holds all the keys in the dictionary
keys = car_milage.keys()

# Printing the keys to verify
print(keys)
print()
vehicle = input("Enter a vehicle to see its mpg: ")

print()

if vehicle in car_milage:
    
    mpg = car_milage[f"{vehicle}"]
    
    print(f"the {vehicle} gets {mpg} mpg.")
    
    print()
else:
    print("car not found")
    
Mpg_to_drive = int(input("How many miles will you drive the Prius? "))



print()

gas_needed = Mpg_to_drive /mpg

print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {Mpg_to_drive:.1f} miles.")
    
    
    
    


