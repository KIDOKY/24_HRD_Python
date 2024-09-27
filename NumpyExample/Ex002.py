import numpy as np

np_value1 = np.array([[1, 1], [2, 2], [3, 3]], dtype = np.int32)
np_value2 = np.insert(np_value1, 1, 4, axis = 0)
print(np_value2)
np.insert(np_value1, 1, 4, axis = 1)
print(np_value2)

#======================================================================
np_value2 = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9], [0, 1, 2]])
print(np_value2)
print(np_value2[0][0])
print(np_value2[3, 0])

np_value3 = np.array([1, 2, 3, 4, 5], dtype = np.int32)
print(f"평균값: {np_value3.mean()}")
print(f"최댓값: {np_value3.max()}")
print(f"최솟값: {np_value3.min()}")

#======================================================================

print(np_value2.flatten())
print(np_value2.T)

np_value4 = np.array([5, 3, 2, 0, 1, 9])
print(np_value4.sort())
print(np_value4)
print(np_value4[::-1])

#======================================================================

# np_value5 = np.array([1, 2, 3])
# np_value6 = np.array([[3, 4, 5], [6, 7, 8]])
# print(np.append([np_value5], np_value6, axis = 1))

#======================================================================

a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 20], [30, 40]])
print(a * b)
print(np.matmul(a, b))
print(a @ b)

#======================================================================

np_value7 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np_value8 = np_value7.reshape(2, -1)
print(np_value8)

#======================================================================

np_value9 = np.random.randn(10) * 10 + 175
print(np_value9)
print(np_value9.round(2))
print(np_value9.astype(int))

#======================================================================

np.random.seed(2024)
np_value10 = np.random.normal(165, 10, (10, 10))
print(np_value10)

#======================================================================

np_value11 = np.array([[1, 2], [1, -3]])
np_value12 = np.linalg.inv(np_value11)
print(np_value12)