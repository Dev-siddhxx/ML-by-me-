import pandas as pd 

sample = pd.read_csv("/home/darks/ML/saple.csv")
print(sample)


# to check th etype of the value of sample we just do the following 
print(type(sample))

# inorder to print the column name we do the following task

print(sample.columns)
# inorder to read specific row we do the following :


sample2 = pd.read_csv("/home/darks/ML/saple.csv", nrows=4)
print(sample2)


# like this we can also do the sam thing with column by the following methods or tasks
 
sample3 = pd.read_csv("/home/darks/ML/saple.csv", usecols=[0, 2,3], nrows=4)
print(sample3)

# in order to skip rows we do th efollwoing task 

sample4 = pd.read_csv("/home/darks/ML/saple.csv", skiprows=[0,1], nrows=2, usecols=[2])# inorder to skip the first row we do this fo rthe secound row then we have put the value 2 

print(sample4)
# inorder to chnage the index nam eas per the column of course we do the following 

print("")
print("")
sample5 = pd.read_csv("/home/darks/ML/saple.csv", index_col=[0], nrows=4, usecols=[0,2,3])# or we can also pass the string format data in order to ak ethe index of your own choice 

print(sample5)


