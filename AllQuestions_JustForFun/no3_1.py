x, y, z = input("Insert 3 numbers: ").split()
x, y, z = int(x), int(y), int(z)

value1, value2, value3 = x+y, x+z, z+y

if value1 > value2 and value1 > value2:
    print(f"Max: {x} + {y} = {value1}")
elif value2 > value1 and value2 > value3:
    print(f"Max: {x} + {z} = {value2}")
elif value3 > value2 and value3 > value1:
    print(f"Max: {y} + {z} = {value3}")