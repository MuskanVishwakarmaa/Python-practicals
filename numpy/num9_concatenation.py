#Q9. Write a NumPy program to concatenate element-wise two arrays of string.

import numpy as np 
a = np.array([[1,2],[3,4]]) 
print ('First array:') 
print (a) 
print ('\n') 
b = np.array([[5,6],[7,8]]) 
print ('Second array:')
print (b) 
print ('\n')  
print ('Joining the two arrays along axis 0:') 
print (np.concatenate((a,b))) 
print ('\n')  
print ('Joining the two arrays along axis 1:') 
print (np.concatenate((a,b),axis = 1))