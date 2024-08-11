n=int(input("Enter rows:"))
# right angled triangles
#1
# for i in range(1,n+1):
#     for j in range(0,i):
#         print(i,end=" ")
#     print("\n")

#2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("\n")

# #3
# a=0
# for i in range(n,0,-1):
#     a+=1
#     for j in range(1,i+1):
#         print(a,end=" ")
#     print("\n")

#4 odd pyramid
# for i in range(1,n+1):
#     for j in range(0,i):
#         print(i*2-1,end=" ")
#     print("\n")

#5
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(j,end=" ")
#     print("\n")

#6
# start = 1
# stop = 2
# current_num = stop
# for row in range(2, 6):
#     for col in range(start, stop):
#         current_num -= 1
#         print(current_num, end=' ')
#     print("")
#     start = stop
#     stop += row
#     current_num = stop

#pascals Triangle
def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()

#
def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)

#7
# n=5
# k=n-1
# for i in range(0,n):
#     for j in range(0,k):
#         print(" ")
#     k-=1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("\r")