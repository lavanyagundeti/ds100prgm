#32q

height = 5  # You can adjust the height as desired


for i in range(1, height + 1, 2):
    spaces = (height - i) // 2
    stars = i
    print(" " * spaces + "*" * stars)

for i in range(height - 2, 0, -2):
    spaces = (height - i) // 2
    stars = i
    print(" " * spaces + "*" * stars)
