#81



my_list = [1, 2, 3, 4, 2, 5, 2]


element_to_remove = 2


my_list = [x for x in my_list if x != element_to_remove]


print(my_list)
