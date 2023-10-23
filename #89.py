#89


list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 5]


is_subset = set(list2).issubset(list1)

if is_subset:
    print("list2 is a subset of list1.")
else:
    print("list2 is not a subset of list1.")
