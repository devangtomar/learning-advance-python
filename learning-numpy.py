# Introduction with NumPy

# why numpy is faster than list

# NumPY : use only fixed type
# 1) Faster to read less bytes of memory
# 2) No type checking..
# 3) Uses contigous memory
# 
# Lists : Size , Reference Count, Object Type, Object Value

# How List are different from NumPy :

# Both can do Insertion, Deletion, Appending, Concatenation etc..
# But much more in NumPy can do...

# Application of NumPy :
# 1) Mathematics 2) Plotting 3) Backend (Pandas, Connect 4, Digital photography) 4) ML  



import numpy as np

a =  np.array([1,2,3])
aa = np.array([1,2,3], dtype='int')
b = np.array([[9.0,1.0,2.0],[6.0,7.0,4.0]])

# Get Dimension : if 1-D or 2-D etc..
print(a.ndim)

# Get Shape 
print(b.shape)

# Get Type
print(a.dtype)
print(aa.dtype)

# Get Size
print(a.itemsize)

# Get total size
print(a.size)
print(a.nbytes) 

# Accessing/Changing Specific elements, rows, columns etc.

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a specific element [r, c]
print(a[1,5])
print(a[1,-2]) # can use negative index...

# Get a specific row and column
print(a[0, :])
print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize]
print(a[0,1:6:2])   # 1st row .. start at 2 (1 as the index) and go till 6 element and need 2 elements..


#Change something
a[1,5] = 20
print(a)


#3-D example...
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


#Intialize different types of array...

# All 0's matrix
a = np.zeros((2,3))
print(a)

# All 1's matrix
a = np.ones((4,2,2), dtype='int32')
print(a)

# Any other number

a = np.full((2,2), 99) # 2 by 2 matrix with 99 as all the elements
print(a)

# Any other number (full_like)
b = np.full_like(a, 4)
print(b)

# Random decimal numbers
a = np.random.rand(4,2)
print(a)

# Random integers values...
a = np.random.randint(-4,9, size=(3,3)) 
print(a)

# Identity matrix
a = np.identity(5)
print(a)

# repeat an array..
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis = 0)
print(r1)


# make a matrix..

output = np.ones((5,5))
print(output)
z = np.zeros((3,3))
z[1,1] = 9 
print(z)

output[1:4,1:4] = z
print(output)

# Be careful when copying arrays!!

a = np.array([1,2,3])
b = a
b[0] = 100
print(b)
print(a)  # contigous memory... that's why.. make use of copy function..

b = a.copy()
b[0] = 400
print(b)
print(a)  # see the changes now...

# Mathematics..

a = np.array([1,2,3,4])
b = np.array([2,2,2,3])
print(a+2)
print(a+b)
print(a**b)
print(np.cos(a))

# Linear algebra..

a = np.ones((2,3))
b = np.full((3,2), 2)

print(np.matmul(a,b))  # matrix multiplication...


# find the determinant...
c = np.identity(3)
print(np.linalg.det(c))



# Statistics...

stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats, axis=0))
print(np.max(stats))
print(np.sum(stats, axis=0))


# Reorganising Arrays..

before = np.array([[1,2,3],[4,5,6]])

print(before.shape)
after = before.reshape((6,1)) # make sure that the number of values in the original numpy arrays..
print(after)

# Vertically stacking vectors..

v1 = np.array([1,2,3])
v2 = np.array([1,2,3])

print(np.vstack([v1,v2,v1,v2]))
print(np.hstack([v1,v2,v1,v2]))

# Miscellaneous things...

# print(np.genfromtxt('data.txt', delimiter=',')) # read from file ...
# filedata = np.genfromtxt('data.txt', delimiter=',')
# # change type...
# filedata = filedata.astype('int32')

# Advanced indexing and Boolean masking...

print(v1>1)  # for boolean recheck...
print(v1[v1>1])  # index only values where value is more than 1... pretty cool right??
a = np.array([1,2,3,4,5,6,7,8])
print(a[[1,2,3]])

print(np.all(a>1, axis=0))
