# Retail Billing with Multiple Discount Rules
amount = float(input("Enter shopping amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0
final_amount = amount - discount
print("Shopping Amount: Rs.", amount)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_amount)