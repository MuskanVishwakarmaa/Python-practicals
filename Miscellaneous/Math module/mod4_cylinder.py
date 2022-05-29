#Q4. Write a Python Program to Calculate the Volume and Surface Area of the cylinder.

Pie = 3.14
radius = float(input('Enter the Radius of a Cylinder: '))
height = float(input('Enter the Height of a Cylinder: '))

S_Area = 2 * Pie * radius * (radius + height)
Volume = Pie * radius * radius * height
L = 2 * Pie * radius * height
T = Pie * radius * radius

print("\n The Surface area of a Cylinder = %.2f" %S_Area)
print(" The Volume of a Cylinder = %.2f" %Volume)
print(" Lateral Surface Area of a Cylinder = %.2f" %L);
print(" Top OR Bottom Surface Area of a Cylinder = %.2f" %T)