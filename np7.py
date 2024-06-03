import numpy as np 
import random
arr = np.random.random(1)
print(arr)
arr2d = np.random.random((2,2))
print(arr2d)
# this is a random value geenrator using numpy in python 
print(np.random.randint(1,10))
x  = [1,2,3,5]
#in order to amke a 2d array using this we do the following 
print(np.random.randint(1,10, (4,4)))


# inorder to make a 3d array using random values in numpy as a python libray is as follows
print(np.random.randint(1,10, (3,3,3)))

# we also function like np.random.rand(3,3) it will create  a 2d array with both positive and negetive values 

print("this is a permutation function it is nothing but a suffle function ")
# in order to permutation 
print(np.random.permutation(x))