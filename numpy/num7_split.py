#Q7. Write a  NumPy program to split the element of a given array with spaces.

import numpy as np
x = np.array(['Python is a programming language'], dtype=np.str)
print("Original Array:")
print(x)
r = np.char.split(x)
print("\nAfter spliting: ")
print(r)
