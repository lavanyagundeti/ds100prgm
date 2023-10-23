#20q

import math


a = float(input("Enter the coefficient 'a': "))
b = float(input("Enter the coefficient 'b': "))
c = float(input("Enter the coefficient 'c': "))


discriminant = b**2 - 4*a*c


if discriminant > 0:
    
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real and distinct roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    
    root = -b / (2*a)
    print("One real root (repeated):")
    print("Root:", root)
else:
    
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-discriminant) / (2*a)
    print("Complex roots:")
    print("Root 1:", realPart, "+", imaginaryPart, "i")
    print("Root 2:", realPart, "-", imaginaryPart, "i")
