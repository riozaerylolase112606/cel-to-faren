# Machine Problem 4: Find the Area of a Triangle Given the Base and Height

def triangle_area(base, height):
    return 0.5 * base * height

# Input from user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = triangle_area(base, height)

print(f"Area of the triangle: {area:.2f}")
