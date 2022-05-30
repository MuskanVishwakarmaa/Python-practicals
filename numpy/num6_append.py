#Q6. Write a Python program to append values to the end of an array.
import numpy as npappend
x = [100, 200, 300]
print("Original array:")
print(x)
x = npappend.append(x, [[400, 500, 610], [700, 810, 900]])
print("After append the values are:")
print(x)