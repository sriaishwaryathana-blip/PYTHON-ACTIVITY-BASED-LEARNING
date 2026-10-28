# Multi-Currency Travel Budget Analysis
budget = float(input("Enter travel budget in rupees: "))
currency = input("Enter currency (USD or EUR): ").upper()
amount = float(input("Enter foreign currency amount: "))
if currency == "USD":
    rate = 85
elif currency == "EUR":
    rate = 95
else:
    rate = 0
    print("Invalid currency")
if rate > 0:
    expense = amount * rate
    remaining = budget - expense
    print("Expense in Rupees: Rs.", expense)
    print("Remaining Budget: Rs.", remaining)
    if remaining >= 0:
        print("Budget is sufficient")
    else:
        print("Budget exceeded")