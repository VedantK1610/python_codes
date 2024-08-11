#numpy is used to convert python list into array
#this is done as numpy array is fast,more memory efficient than pthon list

import numpy as np
import time

size=1000000
l1=range(size)
l2=range(size)
start=time.time()
res1=[(x+y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000) #this time is for python

a1=np.arange(size)
a2=np.arange(size)
start=time.time()
res2=a1+a2
print((time.time()-start)*1000) #this time is for numpy array