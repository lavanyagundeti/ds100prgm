N = int(input("Enter the number of Fibonacci terms to generate: "))

a, b = 0, 1

fib_sequence = [a, b]

for _ in range(N - 2):
    next_term = a + b
    fib_sequence.append(next_term)
    a, b = b, next_term

print("Fibonacci sequence up to", N, "terms:", fib_sequence)
