# Hospital Billing and Patient Classification
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
if age < 18:
    print("Category: Child")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")
print("1. General Checkup - Rs. 500")
print("2. Blood Test - Rs. 800")
print("3. X-Ray - Rs. 1000")
choice = int(input("Enter your choice: "))
if choice == 1:
    bill = 500
elif choice == 2:
    bill = 800
elif choice == 3:
    bill = 1000
else:
    bill = 0
    print("Invalid choice")
if bill > 0:
    print("Patient Name:", name)
    print("Hospital Bill: Rs.", bill)