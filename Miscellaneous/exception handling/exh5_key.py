#Q5. WAP in python to check key error.
myDict = {1: 1, 2: 4, 3: 9}
print("The dictionary is:", myDict)
key=4
print("Key is:",key)
try:
    val=myDict[key]
    print("Value associated to the key is:",val)
except KeyError:
    print("Key not present in Dictionary")
