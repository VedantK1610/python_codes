#0 1 1 2 3 5 8 13

def iterative_fib(n):
    n1=0
    n2=1
    s=n2
    for i in range(n):
        print(s,end=' ')
        s=n1+n2
        n1,n2=n2,s

def recursive_fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return recursive_fib(n-1)+recursive_fib(n-2)


n=int(input())
iterative_fib(n)
print("\n")
for i in range(1,n+1):
    print(recursive_fib(i),end=' ')