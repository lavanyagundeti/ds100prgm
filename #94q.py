text = "programming"

char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

first_non_repeated = None
for char in text:
    if char_count[char] == 1:
        first_non_repeated = char
        break

if first_non_repeated:
    print(f"The first non-repeated character is: {first_non_repeated}")
else:
    print("There are no non-repeated characters in the string.")
