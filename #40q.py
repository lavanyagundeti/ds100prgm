#40q

def is_perfect_number(num):
    if num <= 0:
        return False  # Perfect numbers are positive integers

    divisors = [1]  # 1 is always a proper divisor
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.extend([i, num // i])

    return sum(divisors) == num


number = int(input("Enter a number: "))

if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
