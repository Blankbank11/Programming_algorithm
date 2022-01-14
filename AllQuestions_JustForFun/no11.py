def prime_factor(x):
    prime_factors =[]
    divisor = 2
    while divisor <= x:
        if x % divisor == 0:
            prime_factors.append(divisor)
            x = x/divisor
        else:
            divisor += 1
    return prime_factors

n = int(input("Enter any numbers: "))
print(prime_factor(n))