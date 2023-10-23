#76


my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}


key_to_remove = 'age'


if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"The key '{key_to_remove}' and its value have been removed.")
else:
    print(f"The key '{key_to_remove}' does not exist in the dictionary.")
