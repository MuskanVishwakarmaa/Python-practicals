#Q10. WAP in python to delete the list of keys of dictionary.
D = {'Muskan': 19, 'Mansi': 20, 'Priya': 23, 'Abhay': 27}
keys = ["Mansi", "Abhay"]
 
for k in keys:
    D.pop(k)
print(D)
