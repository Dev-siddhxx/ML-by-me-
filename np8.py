import numpy as np

str1 = "i am genius"
str2 = "siddhxx"
# in order to concat them in an array 


print(np.char.add(str1, str2))


# in order to make it upper case or lower case we do the following 
# upper 
print(np.char.upper(str2))
#lower 
print(np.char.lower(str2))


#in order to make it in center and fill it it with any thing we do the following
print(np.char.center(str1, 60))

# in order to fill it we do the following 


print(np.char.center(str1 , 60, fillchar="#"))


#inorder to do to split the string we do the following 
print(np.char.split(str1))

#in ordre t join the strign by any symbolw e do the following 

print(np.char.join([":", "'"], [str1, str2]))


# then we have replace function in order to use that we do the following things 

print(np.char.replace(str1, "genius",  " a fool")) 


# in order to count a specific alphabet we do the following 

print(np.char.count(str1, "m"))

# in order to find something in the set of given words we do the following , it returns the index value of the element 


print(np.char.find(str2, "i"))