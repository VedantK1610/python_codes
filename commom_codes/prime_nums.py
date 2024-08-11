def prime_num(i):
    if i==0 or i==1:
        return False
    for j in range(2,(i//2)+1):
        if i%j==0:
            return False
    return True

n=int(input())
res=[]
for i in range(1,n+1):
    if prime_num(i):
        res.append(i)
print(res)