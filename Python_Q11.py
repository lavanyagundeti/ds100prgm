#Q11 

num = int(input("Enter a number :"))

if num <= 1 :
	is_prime = False
else:
	is_Prime = True

	for i in range(2, int(num**0.5) +1):
		if num % i == 0:
			is_prime = False
			break
if is_prime:
	print(f"{num} is prime.")
else:
	print(f"{num} not a prime.")