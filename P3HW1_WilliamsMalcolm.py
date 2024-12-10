 #Malcolm Williams

 #12102024

 #p3hw2

 #Brief description of program


# This program takes number grades, determines the average, and displays the letter grade for the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# Print the average and the lowest/highest grades
print("\n---------Results---------")
print(f"{'Lowest grade:':<20} {low}")
print(f"{'Highest grade:':<20} {high}")
print(f"{'Total sum of grades:':<20} {total_sum}")
print(f"{'Average grade:':<20} {avg:.2f}")
print("-------------------------------------")

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')






