#52q


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}


issubset1 = set2.issubset(set1)


issubset2 = set2 <= set1


print("Is set2 a subset of set1 using issubset method:", issubset1)
print("Is set2 a subset of set1 using <= operator:", issubset2)
