#Q5. Write a Python program to select a random element from a list, set, dictionary (value) and a file from a directory.

import random
import os
print("Select a random element from a list:")
elements = [1, 2, 3, 4, 5]
print(random.choice(elements))
print(random.choice(elements))
print(random.choice(elements))
print("\nSelect a random element from a set:")
elements = set([1, 2, 3, 4, 5])
print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))
print("\nSelect a random value from a dictionary:")
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key]) 
print("\nSelect a random file from a directory.:")
print(random.choice(os.listdir("/")))
