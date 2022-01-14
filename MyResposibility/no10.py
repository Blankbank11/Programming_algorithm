list = []
n = int(input("Enter the lenght of list: "))
print("Input numbers: ")

for i in range(n):
    data = int(input())
    list.append(data)

find = int(input("Enter the number you wanna find: "))

if find == list.pop():
    print("Yes")
else:
    print("No")