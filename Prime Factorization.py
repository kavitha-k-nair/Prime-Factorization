def prime(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n%divisor==0:
            factors.append(divisor)
            n = n//divisor
        else:
            divisor += 1

    return factors


n = int(input("Enter a number : "))

result = prime(n)

print(result)

