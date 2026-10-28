# Employee Payroll and Deduction Analysis
name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))
if salary <= 10000:
    deduction = salary * 0.05
elif salary <= 20000:
    deduction = salary * 0.10
else:
    deduction = salary * 0.15
net_salary = salary - deduction
print("Employee Name:", name)
print("Basic Salary: Rs.", salary)
print("Deduction: Rs.", deduction)
print("Net Salary: Rs.", net_salary)