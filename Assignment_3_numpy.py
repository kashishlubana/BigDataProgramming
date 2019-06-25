import numpy as np

#1 How to replace items that satisfy a condition with another value in numpy array?
# Replace all odd numbers in an array with '-1'

print("Question 1: ")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(" Input array:", arr)

print(" Output array:", np.where((arr % 2) == 1, -1, arr))

#2 How to reshape an array?
# Covert 1D array to 2D array with 2 rows

print(" \nQuestion 2: ")

arr = np.arange(10)
print(" Input array:", arr)

newarr = np.reshape(arr, (2, 5))
print(" Output array: \n", newarr)

#3 How to generate custom sequence in numpy without hardcoding
# Reference (https://docs.scipy.org/doc/numpy/reference/generated/numpy.tile.html ),
# (https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html)
print(" \nQuestion 3: ")
arr = np.array([1, 2, 3])
print(" Input array:", arr)
rep = np.repeat(arr, 3)
tile = np.tile(arr, 3)
new_arr = np.r_[rep, tile]
print(" Output array: \n", new_arr)

#4 How to get common values between 2 python numpy arrays
# Get common items between a abd b

print(" \nQuestion 4: ")
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
print("Array1: ", a)
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print("Array2: ", b)
print("Common values between two arrays:", np.intersect1d(a, b))

#5 How to get positions where 2 elements of array match?
# Get the postitions where elements of array a and b match

print(" \nQuestion 5: ")
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
print("Array1: ", a)
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print("Array2: ", b)
match = a == b
print("Indexes where 2 elements of a & b match are:", np.where(match == True))

#6 How to create 2D arrays containing random float values between 5 and 10
# Create 2D array of shape 5*3 to contain random decimal numbers between 5 & 10

print(" \nQuestion 6: ")
print("2D array of shape 5*3 to contain random decimal numbers between 5 & 10: \n",
      np.random.uniform(low=5.0, high=10.0, size=(5, 3)))

#7 How to restrict the number of items printed in output array to 6?
# Limit the number of items in python numpy array to max of 6 elements.

print(" \nQuestion 7: ")

print("Input array:", np.arange(15))
np.set_printoptions(threshold=14)
print("Desired output: ", np.arange(15))

#8 How to pretty print a numpy array by suppressing the scientific notation?


print(" \nQuestion 8: ")

np.random.seed(100)
rand_array = np.random.random([3, 3]) / 1e3
print("Input array: \n", rand_array)
np.set_printoptions(suppress=True)
print("Desired output: \n", np.around(rand_array, decimals=6))


#9 How to swap 2 columns in a 2d numpy array?
# Swap columns 1 and 2 in the array arr


print(" \nQuestion 9: ")

arr = np.arange(9).reshape(3,3)
print("Input array: \n", arr)

arr[:, 0], arr[:, 1] = arr[:, 1], arr[:, 0].copy()
print("Desired Output: \n", arr)


#10 How to swap 2 columns in a 2d numpy array?
# Swap columns 1 and 2 in the array arr


print(" \nQuestion 10: ")


arr = np.arange(9).reshape(3,3)
print("Input array: \n", arr)

arr[0, :], arr[1, :] = arr[1, :], arr[0, :].copy()
print("Desired Output: \n", arr)