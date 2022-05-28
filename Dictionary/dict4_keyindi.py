#Q4. Write a python program to Check for Key in Dictionary Value list.
dict = {'hello' : [{'CS' : 5}, {'Python' : 6}], 'for' : 2, 'CS' : 3} 
 
print("dictionary is : " + str(dict)) 
 
key = "Python"
res = any(key in ele for ele in dict['hello'])
 
print("Is key present in nested dictionary list ?  : " + str(res)) 
