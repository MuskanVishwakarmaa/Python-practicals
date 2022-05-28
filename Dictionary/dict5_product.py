#Q5. Write a python program to find dictionary Keys Product.
dict1 = {'art' : 6, 'is' : 4, 'best' : 7}
dict2 = {'c' : 10, 'is' : 6, 'best' : 10}
 
print("dictionary 1 : " + str(dict1))
print("dictionary 2 : " + str(dict2))
 
res = {key:dict2[key] * dict1.get(key, 0)for key in dict2.keys()}
 
print("The product dictionary is : " + str(res))