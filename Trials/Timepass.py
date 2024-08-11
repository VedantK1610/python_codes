import random as r

l=['vedant','sanket','bunty','akash','yash','fahil','dhiraj','gaurav','safar','srikrishna']

def fun(tmp):
    b = r.randint(0, tmp-1)
    print(l[b])
    del l[b]

a = 10
for i in range(10):
    s=input("Continue?: y/n \n")
    if s=='y':
        fun(a)
        a-=1
    else:
        break