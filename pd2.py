import pandas as pd 

# we have to make a series , inorder to dothat first we have to make a list .
arr = [1,2,3,4,5, 'hello world'," iam a geneius"]
# to convert it into series we do the following task 
series = pd.Series(arr, index=["i", "ii", "iii", "iv", "v", "vi", "vii"])
print(series)# sucessfully created!!


arr1 = [1,2,3,4]
s2 = pd.Series(arr1, index=['a', 'b', 'c', 'd'])
print(s2)

# inorder to change the data type we do the following 
s3 = pd.Series(arr1, dtype=float)
print(s3)
# inorder to give am eto the series we do the following 
s4 = pd.Series(arr1, name="helllo world")
print(s4)
# inorder to make series for single values we do the follwoing things

s5 = pd.Series(1,name="Single scaler values", index=[1,2,3])
print(s5)
# in order to make a series from json or dictionary we do the follwoing 
s6 = pd.Series({
"name": "sai", "age":16
})
print(s6)
#inorder to acess the specific value in the series we do the following 
print(s4[0:3])
#onorder to do amx and min we do the following 
print(max(s4))# similarly we use the min function to find the minimum
# iinorder to add series we do the following things 
print(s4+s3)