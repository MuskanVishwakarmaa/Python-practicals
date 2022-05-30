#Q5. Write a python program to Converting Numpy Array to List.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print('Numpy Array:', arr)
num_list = arr.tolist()
print('List: ', num_list)