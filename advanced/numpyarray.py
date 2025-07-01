import numpy as np

####################################

# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
#
#
# # print(a[0])
# # print(b[1])
#
# c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # print(c)
#
#
# x = np.array([1, 2, 3, 4])
# y = np.array([5, 6, 7, 8])
# print(x+y)

####################################
# a = np.zeros((5,7,3))
# a = np.ones((3,4,6 ))
# a = np.full((3,6,4),4)
# a = np.empty((8,4,2))
# a = np.random.random((2, 3))

# print(a)

####################################

# # x = np.arange(0, 1000, 5)
# x = np.linspace(0, 1000, 101)
# y = np.sin(x)
#
# print(x)
# print(y)


####################################

a = np.array([
    [
        [1,2,3],
        [4,5,6],
    ],
    [
        [10,20,30],
        [40,50,60]
    ]
])

# print(a.shape)
# print(a.size)
# print(a.ndim)
print(a.dtype)

