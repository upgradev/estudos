# Slicing a One-Dimensional Array
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print("slice 1 : ", a[1:5:2])
print("slice 2: ", a[1:6:2])
print("slice 3: ", a[:6:2])
print("slice 4: ", a[1::2])
print("slice 5: ", a[1:6:])

print("--------------------")

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a[0, 0])
print(a[1, 2])
print(a[1, 0])

print("------------")

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(f"First row values : ", a[0:1, :])
print('Alternate values from first row:', '\n', a[0:1, ::2])
print('Second column values :', '\n', a[:, 1::2])

print("----------")
a = np.array([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10],
             [11, 12]], [[13, 14], [15, 16], [17, 18]]])
print(a)
print("First array, first row, first column:", a[0,0,0])
print('First array last column :','\n',a[0,:,1])
# which position start, this case position 1 start [7,8]
print('First two rows for second and third arrays :','\n',a[1:,0:2,0:2])
print("Single array: ", a[1:,0:2,0:2].flatten())

print("Negative Slicing ---------")
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a)
# column
print(a[:, -1:-3:-1])

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("Array original: ","\n", a)
print("Array reverse: ","\n", a[::-1, ::-1])
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("Array original: ","\n", a)
print("Array reverse vertically: ","\n", np.flip(a, axis=1))
print("Array reverse horizontally: ","\n", np.flip(a, axis=0))