#Q8. Write a NumPy program to count the number of "n" in a given array, element-wise.

import numpy as np
x1 = np.array(['my','name','is','Muskan'], dtype=np.str)
print("\nOriginal Array:")
print(x1)
print("Number of ‘n’:")
r = np.char.count(x1, "n")
print(r)
