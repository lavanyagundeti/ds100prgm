#53q



my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


frequency_dict = {}


for element in my_list:
    if element in frequency_dict:
        frequency_dict[element] += 1
    else:
        frequency_dict[element] = 1

for key, value in frequency_dict.items():
    print(f"{key}: {value}")
