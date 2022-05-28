#Q8. WAP in python to replace values in dict1 from dict2, if key is present in dict2 - Using loops
Dict1 = {'first_name' : 'Muskan', 'age' : 19, 'height' : 5.0}
Dict2 = {'age' : 22, 'course' : 'BTech'}
for key in Dict1:
  if key in Dict2:
    Dict1[key] = Dict2[key]
print("The original dictionary: " + str(Dict1))
print("The updated dictionary: " + str(Dict2))