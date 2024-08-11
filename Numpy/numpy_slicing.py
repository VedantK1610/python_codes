import numpy as np
a=np.array([[7,8,9],[10,11,12]])
print(a[0:1])
print("\n")
b=np.array([[1,2],[3,4],[5,6]])
b=b.reshape(2,3)
print(b)
print(b[0:2,1]) #go to two rows and return index 1 element from both rows

#to put one array on another like stack
print("\n")
print(np.vstack((b,a)))
print("\n")
print(np.hstack((b,a)))

print("\n")
c=np.arange(12).reshape(3,4)
d=c>4
print(d)
print(c[d])
# c[d]=-1   #will replace number with -1 with satisfies d condition
# print(c)

