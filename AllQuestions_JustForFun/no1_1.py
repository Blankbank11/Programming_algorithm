before = str(input("Enter a string: "))
after =""
for i in before:
    if i not in after:
        after = after + i
print(after)