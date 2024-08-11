import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print("dimensions of array:",a.ndim)
print("size of each element:",a.itemsize)
print("no of elements:",a.size)
print("rows and colums are:",a.shape)

#to create array with 0 intialization
#b=np.zeros((3,4),dtype=int) #pass row and column value
#print(b)

#to generate array that is linear spaced betw two nums
# b=np.linspace(1,5,10)
# print(b)

# a=a.reshape(2,3)

# a=a.ravel() #to flat your array i.e. 1 dimentional

#print(a.min()) and also max
# print(a.sum())

print(a)
print("sum along x-axis axis:",a.sum(axis=1))
print("sum along y-axis axis:",a.sum(axis=0))

