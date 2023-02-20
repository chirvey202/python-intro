#a function to return the area of a circle
from math import pi
from math import pow
radius = int((input("Enter the radius of the cylinder : ")))
r = int((input("Enter the radius of the sphere : ")))
height = int((input("Enter the height of the cylinder : ")))

def volume_of_a_cylinder(radius,height):
    cross_sectional_area = pi * pow(radius, 2)
    volume = cross_sectional_area* height
    return volume
    
print("Volume of a cylinder :",volume_of_a_cylinder(radius, height))


#volume of a sphere


def volume_of_a_sphere(r):
    volume = 4/3*(pi * pow(r, 3))
    return volume

print("volume of a sphere:",volume_of_a_sphere(r))
    

