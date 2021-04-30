income_tax=0

id = int(input("Enter Employee id: "))
basic_salary = int(input("Enter monthly gross salary: "))
allowance = int(input("Enter allowance: "))

gross_salary = basic_salary+allowance

if gross_salary<=5000:
    income_tax = 0
elif gross_salary<=10000:
    income_tax = 0.1 * gross_salary
elif gross_salary<=20000:
    income_tax = 0.2 * gross_salary
else :
    income_tax = 0.3 * gross_salary

net_pay = gross_salary-income_tax

print("Employee id: {}\nBasic Salary: {}\nAllowance: {}\nGross Pay: {}\nIncome Tax: {}\nNet pay: {}". format(id,basic_salary,allowance,gross_salary,income_tax,net_pay))
