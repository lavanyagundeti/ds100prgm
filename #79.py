#79


words = ["apple", "banana", "cherry", "date", "fig", "grape"]


longest_length = 0


for word in words:
    if len(word) > longest_length:
        longest_length = len(word)


print("Length of the longest word:", longest_length)
