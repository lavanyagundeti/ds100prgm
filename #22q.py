#22q

my_list = [4, 2, 9, 7, 1, 12, 5]
largest = my_list[0]
smallest = my_list[0]

for num in my_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest element:", largest)
print("Smallest element:", smallest)
