#Your Name
#Date
#Assignment Name
#A brief description of the project


while True:
    name = input("Enter employee's name or type 'done' to stop: ")
    
    if name.lower() == 'done':
        print("Process terminated.")
        break  # This stops the loop
    else:
        print(f"Employee '{name}' entered.")

Hours_worked = int(input('How many hours did Nancy Drew work?: '))
Employee_payrate = float(input("What is Nancy Drew's pay rate?': "))


print(f'name.lower:    {name.lower}\n')
print("Hours Worked" + (" " * 4) +"payrate" + (" " * 4) + "Overtime" + (" " * 4) + "OverTime Pay" + (" " * 4) + "RegHour Pay" + (" " * 4) + "Gross Pay" )
print("-" * 79)
overtime = Hours_worked - 40
overtime_pay = (Employee_payrate * 1.5)  * overtime
Reghour_pay = Employee_payrate * 40
Gross_pay = Reghour_pay + overtime_pay
print(f'{Hours_worked:.1f}' + (" " * 10) + f'{Employee_payrate:.1f}' + (" " * 10) + f'{overtime:.1f}' + (" " * 10) + f'{overtime_pay:.2f}' + (" " * 10) + f'${Reghour_pay:.2f}' + (" " * 10) + f'${Gross_pay:.2f}' + (" " * 10))


