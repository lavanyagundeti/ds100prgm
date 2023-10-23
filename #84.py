#84


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'c': 3, 'd': 4, 'e': 5, 'f': 6}

 
common_elements = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}


print("Common elements between the dictionaries:")
for key, value in common_elements.items():
    print(f"{key}: {value}")
