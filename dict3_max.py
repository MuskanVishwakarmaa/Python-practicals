#Q3. Write a python program to print Keys with Maximum value from dictionary. 
dict = {'hello' : 2, 'world' : 1, 'Python' : 3, 'computer': 2}
 
print("The new dictionary is : " + str(dict))
 
temp = max(dict.values())
res = [key for key in dict if dict[key] == temp]
 
print("Keys with maximum values are : " + str(res))