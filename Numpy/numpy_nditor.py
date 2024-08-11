import numpy as np

a=np.arange(12).reshape(3,4)
print(a)
# for x in np.nditer(a,order='C'): #it will return rowwise elements
#     print(x)
#

# for x in np.nditer(a,order='F'):  #return column wise element and F stands for Fortran
#     print(x)

# for x in np.nditer(a,order='F',flags=['external_loop']):  #return column wise row and F stands for Fortran
#      print(x)

# for x in np.nditer(a,op_flags=['readwrite']): #it modifies the original array with new values
#     x[...]=x*x
# print(a)

b=np.array([5,7,11]).reshape(3,1)
print(b)
for x,y in np.nditer([a,b]):
    print(x,y)