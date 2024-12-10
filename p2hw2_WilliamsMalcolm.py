#Malcolm Williams
#1232024
#p2hw2
#Assignment assess student understanding of Lists



# Input grades for all six modules
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Put all grades into a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculate the required results
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Output the results
print("\n----------Results--------")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {sum_of_grades}")
print(f"Average: {average_grade:.2f}")
print("---------------------------------------")
