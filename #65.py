#65

def is_sorted_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [3, 1, 2, 4, 5]


if is_sorted_ascending(sorted_list):
    print("The 'sorted_list' is sorted in ascending order.")
else:
    print("The 'sorted_list' is not sorted in ascending order.")

if is_sorted_ascending(unsorted
