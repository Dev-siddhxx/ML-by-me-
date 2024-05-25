import numpy as np




# Normal syntax for the arange fuction in numpy in python
# np.arange(start_value, end_value, no.of_steps_it _will_jimp) 
arr1d = np.arange(2,25,2)
print(arr1d)
print(arr1d.size)




# Line space :  according to this function it tells the user to give a range in side which it will create some numbers inside that ranage 
# Syntax : np.linespace(start_value, end_value, the_no.of_number_the_user_want_to_get)


arr1= np.linspace(1,5,2)
print(arr1)

# reshape fucntion : it helps in converting a 1d array into 2d array or 3d array 
# 
print("This is a 2d array", arr1d.reshape(6,2))

print("This is an 3d array : ", arr1d.reshape(2,3,2))



# to do all this thing in one line we do teh following 
arr = np.arange(1,13, 1).reshape(2,3,2)
print(arr)




# Ravel , coverts any type of array into 1d array 
 

print(arr.ravel())



# Transpose function it interchanges the row aand column 

print("this is the transpose function")
print(arr.transpose())