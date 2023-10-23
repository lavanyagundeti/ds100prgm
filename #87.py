#87

my_list = [10, 20, 30, 40, 50, 30]


element_to_find = 30


if element_to_find in my_list:
    index = my_list.index(element_to_find)
    print(f"The element {element_to_find} is at index {index}.")
else:
    print(f"The element {element_to_find} is not in the list.")
