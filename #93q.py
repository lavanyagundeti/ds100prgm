list_of_lists = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [7, 8, 9]]

unique_elements = list(set(item for sublist in list_of_lists for item in sublist))

print("Unique elements:", unique_elements)
