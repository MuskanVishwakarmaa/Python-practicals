#Q3. Write a Python program to shuffle the elements of a given list.

import random
l = list(range(5))
print(l)
# [0, 1, 2, 3, 4]
random.shuffle(l)
print(l)
# [1, 0, 4, 3, 2]
