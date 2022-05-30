#Q2. Write a Python program to generate a float between 0 and 1, inclusive and generate a random float within a specific range.

import random 
print("Generate a float between 0 and 1, inclusive:")
print(random.uniform(0, 1))
print("\nGenerate a random float within a range:")
random_float = random.uniform(1.0, 3.0)
print(random_float)