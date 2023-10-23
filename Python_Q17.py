#Q17

N = int(input("Enter the value of N :")

even_sum = 0

for i in range(2, N + 1, 2) :
	even_sum += i

print(f"The Even numbers from 1 to {N} : {even_sum}")
