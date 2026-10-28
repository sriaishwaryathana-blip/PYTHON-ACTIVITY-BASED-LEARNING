#material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
other = float(input("Enter other costs: "))
quantity = int(input("Enter number of products: "))
price = float(input("Enter selling price per product: "))
material=int(input("enter the material cost:"))
total_cost = material + labour + other
total_sales = quantity * price
profit = total_sales - total_cost

print("Total Manufacturing Cost: Rs.", total_cost)
print("Total Sales: Rs.", total_sales)
print("Profit/Loss: Rs.", profit)

if profit > 0:
    print("Profit")
elif profit < 0:
    print("Loss")
else:
    print("No Profit, No Loss")