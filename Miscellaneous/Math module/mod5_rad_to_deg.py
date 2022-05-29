#Q5. Write a Python program to convert radian to degree.

import math
def degree(x):
    pi=math.pi
    degree=(x*180)/pi
    return degree
print("Value in Degree:",degree(1.5))