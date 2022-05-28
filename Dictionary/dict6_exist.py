#Q6. WAP in python to check if a Given Key Already Exists in Dictionary

D1 = {'first_name' : 'Muskan', 'age' : 19, 'height' : 5.0 , 'college name' : 'GLAU', 'course': 'BTech'}
 
def check_key(x):
  if x in D1:
      return 'Yes'
  else:
      return 'No'
print("Is key named 'first_name' present?", check_key('first_name'))
print("Is key named 'course' present?", check_key('branch'))
