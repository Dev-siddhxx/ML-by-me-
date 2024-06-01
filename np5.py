import numpy as np 
arr1 = np.arange(1,17).reshape((4,4))
arr2 = np.arange(17,33).reshape((4,4))
# coloumn wise concatination 
concat = np.concatenate((arr1,arr2))
print(concat)
# row wise conactenation (axis = 0 represents column and axis = 1 represents row)
conacat2 = np.concatenate((arr1, arr2), axis=1)
print(conacat2)
# to do the sa thing with out any axis 
# we use vstack and hstack 

print(np.vstack((arr1, arr2)))# for vertical or column wise 

print(np.hstack((arr1,arr2)))# for horizontal or row wise conacatenations 

# the split function 

print(np.split(arr1, 2, axis=1))

arr1d = np.arange(1,11)
print(np.split(arr1d, [3, 7]))
