#Q16

num = int(input("Enter a number :"))

num_str = str(num)

if num_str == num_str[::-1] :
	print("The number is palindrome")
else:
	print("The number is not a palindrome")
