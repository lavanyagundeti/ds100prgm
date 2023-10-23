#69


my_dict = {'a': 10, 'b': 25, 'c': 15, 'd': 25, 'e': 5}


max_value = max(my_dict.values())
keys_with_highest_values = [key for key, value in my_dict.items() if value == max_value]

print(f"The keys with the highest values are: {keys_with_highest_values}")
