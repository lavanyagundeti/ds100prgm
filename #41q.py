#41q

def nth_term_of_ap(a1, n, d):
    if n < 1:
        return "Invalid value of n. It should be a positive integer."

    nth_term = a1 + (n - 1) * d
    return nth_term


a1 = float(input("Enter the first term (a1): "))
n = int(input("Enter the term position (n): "))
d = float(input("Enter the common difference (d): "))

result = nth_term_of_ap(a1, n, d)
if isinstance(result, str):
    print(result)
else:
    print(f"The {n}th term of the arithmetic progression is: {result:.2f}")
