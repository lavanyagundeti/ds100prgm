#28q


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

 
def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    
    num1 = float(input("Enter the first number: "))

    
    operation = input("Enter the operation (+, -, *, /): ")

   
    num2 = float(input("Enter the second number: "))

    
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        continue

    
    print("Result: ", result)

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break
