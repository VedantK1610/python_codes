def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

n=5
for i in range(1,n+1):
    print(factorial(i),end=' ')