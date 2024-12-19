import numpy as np 

# my_array = np.array([[1,2,3,56,5]], np.int8) 
# a2 = np.array(['hi',4,5], )
# # print(my_array)
# print(my_array.shape)
# print(my_array[0])
# print(my_array.dtype)
# print(a2)

# arr = np.zeros((2,3))
# print(arr)
# rng = np.arange((8))
# print(rng)

# lin = np.linspace(1,10,5)
# print(lin)
# x=np.arange(99)
# x.reshape(3,33)
# print(x)

#axis in numpy 
# ar = np.array([1,2,3],[4,5,6],[6,5,4])  it is a wrong method forcreating a array  because  it takes a list to or tuple to make an array
#                                but you are giving it a 3 list like [],[],[]
#                                 you need to do it like that [[],[],[]]

ar = np.array([[1,2,5],
               [3,5,4],
               [4,3,3]])

# print(ar.argmin(axis=1))
# print(np.sqrt(ar))
print(ar.tolist())
print(ar)


# there are some basic function of numpy   ar.size    ar.nbytes    ar.argmax
# ar.argmin   ar.argmax(aix=1)  ar.argmax(axi=0)  ar.argmin(axis=0)    ar.argmin(axis=1)
# ar.argsort()


# print(ar.sum(axis = 1))
# ar.flat
# print(ar)
# ar.nbytes
# print(ar.itemsize) 

for fg in ar.flat:
    print(fg)

