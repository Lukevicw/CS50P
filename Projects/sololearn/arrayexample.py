import numpy as np

print("Arrays in their glory")
arr = np.array([1, 2, 3, 4, 5])

arr_2D = np.array([[1, 2, 3], [4, 5, 6]])

arr_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

print("Different Dimensions")
print(type(arr))

print(arr_2D)
print(arr_3D)

print("Count dimensions")
a = np.array(arr)
b = np.array(arr_2D)
c = np.array(arr_3D)

print(a.ndim)
print(b.ndim)
print(c.ndim)

print("Adding arrays")
addarray = np.array([1, 2, 3, 4])
print(addarray[2] + addarray[3])

print("Accessing 2D Arrays")
acc = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', acc[0, 1])
