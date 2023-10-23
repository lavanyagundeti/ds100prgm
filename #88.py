#88


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
merged_dict = {}


for key, value in dict1.items():
    if key in dict2:
        merged_dict[key] = [value, dict2[key]]
    else:
        merged_dict[key] = [value]


for key, value in dict2.items():
    if key not in merged_dict:
        merged_dict[key] = [value]


print("Merged Dictionary with lists for duplicate keys:")
print(merged_dict)
