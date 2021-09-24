import numpy as np
# create array numpy
print("simple array: ", np.array([1, 2, 3, 4]))
print("-------------")
# Here, we have included integer values and the dtype argument is used to specify the data type:
print("array data type: ", np.array([1, 2, 3, 4], dtype=np.float32))
print("-------------")
# You can also create multidimensional arrays:
print("array multi: ", np.array([[1, 2, 3, 4], [5, 6, 7, 8]]))
print("-------------")
# array of zeros
print("numpy array Zeros", np.zeros(5))
print("array zeros multi: ", np.zeros((2, 3)))
print("array ones: ", np.ones(5, dtype=np.int32))
print("-------------")
# random number in ndarray
print("random from [0,1]: ", np.random.rand(2, 3))
print("-------------")
# You can even create arrays with any value you want with the np.full() method, ensuring the shape of the
# array you want is passed in along with the desired value:
print("choice type of array: ", np.full((2, 2), 7))
print("-------------")
# The np.eye() method is another good one that returns 1s on the diagonal and 0s everywhere else. More formally known as an Identity Matrix,
# it is a square matric with an N x N shape,
# meaning there is the same number of rows as columns. Below is a 3 x 3 IMatrix:
print("identity matrix: ", np.eye(3, 3))
print("-------------")
# Determining how many axes or dimensions the ndarray has is easily done using an attribute called ndims:

a = np.array([[5, 10, 15], [20, 25, 20]])
print("Array:", "\n", a)
print("Dimensions:", "\n", a.ndim)
print("-------------")
# NumPy Array Shape
# The array shape is an array attribute showing the number of rows with elements along
# each of the dimensions. The shape can be further indexed so the result shows the value on each dimension:
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:", a)
print("Shape:", a.shape)
print("Rows:", a.shape[0])
print("columns:", a.shape[1])
print("-------------")
# The size attribute tells you the number of values in your array by multiplying the number of rows by columns:
a = np.array([[5, 10, 15], [20, 25, 20]])
print("size array a: ", a.size)
print("Manual determination of size of array: ", a.shape[0]*a.shape[1])

print("----------")
# Reshaping an Array
# You can use the np.reshape() method to reshape your ndarray without changing any of the data in it:
a = np.array([3, 6, 9, 12])
print("array: ", a)
print("reshape: ", np.reshape(a, (2, 2)))
print("-------------")

a = np.array([3, 6, 9, 12, 18, 24])
print("array: ", a)
print("reshape three rows: ", np.reshape(a, (3, -1)))
print("reshape  three cols: ", np.reshape(a, (-1, 3)))
print("---------------")

# flattening arrays
# There may be times when you want to collapse a multidimensional array into a single-dimensional array.
# There are two methods you can use for this – flatten() or ravel():
a = np.ones((2, 2))
b = a.flatten()
c = a.ravel()
print("Array: ", a)
print("Array original shape: ", a.shape)
print("shape after flatten: ", b.shape)
print("Array: ", b)
print('Shape after ravel :', c.shape)
print('Array :', '\n', c)
print("---------------")

# The transpose() method is a reshaping method that takes the input array, swapping the row values with the columns and vice versa:
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.transpose(a)
print("Original", a.shape, "-", a)
print("Expand along columns: ", b.shape, "-", b)
print("------------")
# Expanding a ndarray involves adding new axes. This is done with the method called expand_dims(), passing the array and the axis you want to expand along:
# expand dimensions
a = np.array([1, 2, 3])
b = np.expand_dims(a, axis=0)
c = np.expand_dims(a, axis=1)
print('Original:', '\n', 'Shape', a.shape, '\n', a)
print('Expand along columns:', '\n', 'Shape', b.shape, '\n', b)
print('Expand along rows:', '\n', 'Shape', c.shape, '\n', c)
