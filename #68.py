#68


ict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}


result = dict1.copy()


for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print("Merged dictionary with summed
