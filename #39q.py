#39q

import math


def cube_volume(side_length):
    return side_length**3


def sphere_volume(radius):
    return (4/3) * math.pi * radius**3


def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

shape = input("Enter the shape (cube, sphere, or cylinder): ").lower()

if shape == "cube":
    side_length = float(input("Enter the side length of the cube: "))
    volume = cube_volume(side_length)
    print(f"The volume of the cube is {volume:.2f} cubic units")
elif shape == "sphere":
    radius = float(input("Enter the radius of the sphere: "))
    volume = sphere_volume(radius)
    print(f"The volume of the sphere is {volume:.2f} cubic units")
elif shape == "cylinder":
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = cylinder_volume(radius, height)
    print(f"The volume of the cylinder is {volume:.2f} cubic units")
else:
    print("Invalid shape. Please enter 'cube', 'sphere', or 'cylinder'.")
