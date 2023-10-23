#42q

import math

def area_of_circle_segment(radius, angle_degrees):
    
    angle_radians = math.radians(angle_degrees)

   
    area = (radius**2 / 2) * (angle_radians - math.sin(angle_radians))

    return area


radius = float(input("Enter the radius of the circle: "))
angle_degrees = float(input("Enter the angle of the segment in degrees: "))

if angle_degrees < 0 or angle_degrees > 360:
    print("Invalid angle. Angle must be between 0 and 360 degrees.")
else:
    segment_area = area_of_circle_segment(radius, angle_degrees)
    print(f"The area of the circle segment is: {segment_area:.2f} square units")
