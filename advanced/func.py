import numpy as np

# a = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.exp(a))
# print(np.sqrt(a))
# print(np.log(a))

#############################

# print(a.sum())
# print(a.max())
# print(a.min())
# print(a.mean())
# print(np.median(a))
# print(np.std(a))

#############################

# a = np.array([
#     [1,2,3,7],
#     [4,5,6,7],
#     [7,8,9,7]
# ])
#
# # a = a.reshape((2,3,2))
# # print(a)
#
# # print(a.flatten())
# # print(a.transpose())
#
# # for x in a.flat:
# #     print(x)
# # print(a.flat[7])

#############################

# a = np.array([
#     [1,2,3,7],
#     [4,5,6,7],
#     [7,8,9,7],
#     [10,11,12,8]
# ])

# b = np.array([
#     [10,20,30,40],
#     [50,60,70,80],
#     [70,80,10,20],
# ])
#
# # c = np.concatenate((a, b))
# # c2 = np.hstack((a,b))
# # c3 = np.vstack((a,b))
# # # print(c)
# # print(c2)
# # print(c3)
#
# # print(np.split(a,2))
# print(np.hsplit(a,2))

#############################

a = np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7],
    [10,11,12,8]
])

b = [10,20,30,40]

# a = np.append(a,b)
# print(a)

# a = np.append(a,[b], axis=0)
# print(a)

a = np.insert(a,2,b, axis=1)
print(a)

