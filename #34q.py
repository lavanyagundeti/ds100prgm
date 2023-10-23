#34q

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


num = int(input("Enter a number: "))

if num < 2:
    print("Prime factors are not defined for numbers less than 2.")
else:
    factors = prime_factors(num)
    print("Prime factors of", num, "are:", factors)
