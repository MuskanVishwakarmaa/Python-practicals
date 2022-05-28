#Q1. Write a python program to Concatenate Dictionary string values.  
dict1 = {'A' : 'a', 'is' : 'b', 'and' : 'c'}
dict2 = {'A' : '1', 'is' : '2', 'and' : '3'}
 
print("dictionary 1 : " + str(dict1))
print("dictionary 2 : " + str(dict2))
 
res = {key:dict1[key] + dict2.get(key, '') for key in dict1.keys()}
 
print("The string concatenation of dictionary is : " + str(res))
