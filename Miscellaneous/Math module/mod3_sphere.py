#Q3. Write a Python Program to Calculate the Volume and Surface Area of the Sphere.

Pie = 3.14
radius = float(input("Enter the Radius of a Sphere: "))
Area =  4 * Pie * radius * radius
Volume = (4 / 3) * Pie * radius * radius * radius
print("\nThe Surface area of a Sphere = %.2f" %Area)
print("\nThe Volume of a Sphere = %.2f" %Volume)