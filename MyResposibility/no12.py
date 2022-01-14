number = int(input("Enter the number: "))

factorial = 1
sum = 0
if number < 0:
    print("Please insert positive number")
else:
    for i in range(number, 1, -1):
        factorial = factorial * i

print("Factorial of", number ,"= ", factorial)

while factorial > 0:
    sum = sum + factorial % 10
    factorial = factorial // 10

print("Sum of digit = ", sum )