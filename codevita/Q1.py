m1=int(input())
m2=int(input())
N=int(input())
populations=list(map(int,input().split()))
t1=0
t2=0
populations.sort(reverse=True)

for p in populations:
    if t1<=t2:
        t1+=p*m1
    else:
        t2+=p*m2

res=max(t1,t2)
print(res,end=' ')