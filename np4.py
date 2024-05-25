import numpy as np
arr = np.arange(1,101).reshape(10,10)
print(arr)


print("to get the first element ")



print(arr[0][0])



print("to get all the elements in the row") 


print(arr[0])


print("to get all the elements in the coloumn") 


print(arr[:, 0])


print("to convert it into 2s array we do the following task :")


print(arr[:, 0:1])


print("to get acess over particular row or perticular coloumn we do the following")


print(arr[1:4, 1:4])


print("to check itemsize of the array ")


print(arr.itemsize)


print("to check the data type of te array ")


print(arr.dtype)

