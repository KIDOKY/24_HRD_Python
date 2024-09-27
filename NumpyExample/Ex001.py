# import numpy as np
# list_a = [1, 2, 3, 4, 5]
# print(type(list_a))
# np_array1 = np.array(list_a)
# print(type(np_array1))
# print(list_a)
# print(np_array1)
# # print(list_a.shape)
# print(np_array1.shape)

#==========================================
import numpy as np
a = np.array([2, 3, 4])
list_a = [1, 2, 3, 4, 5]
print(type(list_a))
np_array1 = np.array(list_a, dtype = np.int32)
print(type(np_array1))
print(list_a)
print(np_array1)
print(np_array1.shape, np_array1.ndim, np_array1.dtype, np_array1.itemsize, np_array1.size)

#==========================================

np_array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(np_array2.shape)
print(np_array2)
print(np_array2.ndim, np_array2.itemsize, np_array2.size)

#==========================================

np_array3 = np.array([10, 20, 30])
result = np_array3 * 3
print(result)

result2 = np_array3 + 10
print(result2)

#==========================================

b = np.array([[10, 20, 30], [40, 50, 60]])
c = np.array([2, 3, 4])

print(b + c)
print(b * c)

#==========================================

print(np.eye(20))

#==========================================

print(10 * np.eye(4))

np_array4 = np.arange(0, 10)
print(np_array4)
np_array5 = np_array4.reshape((5, 2))
print(np_array5)

np_array6 = np.linspace(0, 10, 1000)
print(np_array6)

#==========================================