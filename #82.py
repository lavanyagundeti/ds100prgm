#82  


my_list = [12, 35, 1, 10, 34, 6]


sorted_list = sorted(my_list)


if len(sorted_list) >= 2:
    
    second_largest = sorted_list[-2]
    print("The second largest element is:", second_largest)
else:
    print("The list does not have a second largest element.")
