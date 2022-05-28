#Q9. WAP in python to changing the keys of dictionary.
Dict1 = {'Muskan': 19, 'Mansi': 20, 'Priya': 23, 'Abhay': 27}
print("The original dictionary is =", Dict1)
Dict1['Sahil'] = Dict1['Mansi']
del Dict1['Mansi']
print ("Dictionary D1 after changing key 'Mansi'=", str(Dict1))
Dict1['Riya'] = Dict1.pop('Priya')
print ("Dictionary Dict1 after changing key 'Priya'=", str(Dict1))
new_keyslist = ['doremon', 'shincham', 'tom', 'jerry']
final_Dict1 = dict(zip(new_keyslist, list(Dict1.values())))
print ("Dictionary Dict1 after changing all keys=", str(final_Dict1))