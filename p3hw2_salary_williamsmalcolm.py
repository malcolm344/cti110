#Your Name
#Date
#Assignment Name
#A brief description of the project

# Enter valubles for name, hours worked, pay rate
Employee_name = str(input("Enter employee's name: "))
Hours_worked = int(input('Enter number of hours worked: '))
Employee_payrate = float(input("Enter employee's pay rate: "))

#format
print("-" * 31)
print(f'Employee name:    {Employee_name}\n')
print("Hours Worked" + (" " * 4) +"payrate" + (" " * 4) + "Overtime" + (" " * 4) + "OverTime Pay" + (" " * 4) + "RegHour Pay" + (" " * 4) + "Gross Pay" )
print("-" * 85)

#calculations
overtime = Hours_worked - 40
overtime_pay = (Employee_payrate * 1.5)  * overtime
Reghour_pay = Employee_payrate * 40
Gross_pay = Reghour_pay + overtime_pay

 #output
print(f'{Hours_worked:.1f}' + (" " * 10) + f'{Employee_payrate:.1f}' + (" " * 10) + f'{overtime:.1f}' + (" " * 10) + f'{overtime_pay:.2f}' + (" " * 10) + f'${Reghour_pay:.2f}' + (" " * 10) + f'${Gross_pay:.2f}' + (" " * 10))
