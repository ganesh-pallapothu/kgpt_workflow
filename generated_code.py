
import math

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

# 3D Figures
def cube_volume(side):
    return side ** 3

def cube_surface_area(side):
    return 6 * (side ** 2)

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

def sphere_surface_area(radius):
    return 4 * math.pi * (radius ** 2)

def cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def main():
    print("Geometry Calculator")
    print("1. Rectangle (2D)")
    print("2. Circle (2D)")
    print("3. Triangle (2D)")
    print("4. Cube (3D)")
    print("5. Sphere (3D)")
    print("6. Cylinder (3D)")
    choice = input("Choose a figure (1-6): ")

    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area:", rectangle_area(length, width))
        print("Perimeter:", rectangle_perimeter(length, width))
    elif choice == "2":
        radius = float(input("Enter radius: "))
        print("Area:", circle_area(radius))
        print("Circumference:", circle_circumference(radius))
    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        print("Area:", triangle_area(base, height))
        print("Perimeter:", triangle_perimeter(a, b, c))
    elif choice == "4":
        side = float(input("Enter side length: "))
        print("Volume:", cube_volume(side))
        print("Surface Area:", cube_surface_area(side))
    elif choice == "5":
        radius = float(input("Enter radius: "))
        print("Volume:", sphere_volume(radius))
        print("Surface Area:", sphere_surface_area(radius))
    elif choice == "6":
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        print("Volume:", cylinder_volume(radius, height))
        print("Surface Area:", cylinder_surface_area(radius, height))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
