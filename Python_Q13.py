#Q13
n1 = int(input("Enter the 1st number :"))
n2 = int(input("Enter the 2nd number :"))
n3 = int(input("Enter the 3rd number :"))

if n1 >= n2:
	if n1 >= n3:
		largest = n1
	else:
		largest = n3
else:
	if n2 >= n3:
		largest = n2
	else:
		largest = n3

print(f"The largest number of {n1}, {n2} and {n3} {largest}")
