# Campus Event Financial Planning
budget = float(input("Enter event budget: "))
food = float(input("Enter food expenses: "))
decoration = float(input("Enter decoration expenses: "))
other = float(input("Enter other expenses: "))
total = food + decoration + other
remaining = budget - total
print("Total Budget: Rs.", budget)
print("Total Expenses: Rs.", total)
print("Remaining Amount: Rs.", remaining)
if remaining > 0:
    print("Budget is sufficient")
elif remaining < 0:
    print("Budget exceeded")
else:
    print("Budget 100fully used")