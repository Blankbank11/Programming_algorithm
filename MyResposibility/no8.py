
n = int(input("Enter the number of your menu: "))

if 0 < n < 10:
    price = n * 20
elif n > 10:
    price = n * 8

print(f"price: {price} dollars")