#29q


total = 0

while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    
    if user_input.lower() == 'q':
        break

    try:
        
        number = float(user_input)
        total += number
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

print("Sum of the entered numbers:", total)
