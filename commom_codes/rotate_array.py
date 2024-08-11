def rotate_array(a,d):
    c=1
    i=0
    n=len(a)
    while c<=d:
        last = a[0]
        for i in range(n-1):
            a[i]=a[i+1]
        a[n-1]=last
        c+=1
    return a


a=[1,2,3,4,5,6,7]
d=2
print(rotate_array(a,d))