# Create a list of elements
elements = [2, 4, 5, 2, 4, 6, 4, 7, 2]

element_count = {}
for element in elements:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

mode = max(element_count, key=element_count.get)

print(f"The mode of the list is {mode} with {element_count[mode]} occurrences.")
