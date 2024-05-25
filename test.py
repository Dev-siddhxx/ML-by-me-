import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])

print("Original array: ", arr)

# Get the shape of the array
print("Shape of the array: ", arr.shape)

# Get the data type of the array
print("Data type of the array: ", arr.dtype)

# Create a 2D numpy array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print("\n2D array: ", arr2d)

# Get the shape of the 2D array
print("Shape of the 2D array: ", arr2d.shape)

# Get the data type of the 2D array
print("Data type of the 2D array: ", arr2d.dtype)

# Perform basic operations on the arrays
print("\nSum of the array: ", np.sum(arr))
print("Mean of the array: ", np.mean(arr))
print("Standard deviation of the array: ", np.std(arr))

# Perform basic operations on the 2D array
print("\nSum of the 2D array: ", np.sum(arr2d))
print("Mean of the 2D array: ", np.mean(arr2d))
print("Standard deviation of the 2D array: ", np.std(arr2d))