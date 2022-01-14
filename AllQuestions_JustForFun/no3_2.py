list = [int(i) for i in input("Enter any numbers: ").split()]
list = sorted(list)

max1 = list[-1]
max2 = list[-2]
result = max1 + max2
print(f"Max: {max1} + {max2} = {result}")

