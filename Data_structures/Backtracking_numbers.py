'''
generate all possible numbers created from only nums 1,2 and numbers should be in
increasing order.
'''
def print_nums(N,arr,i):
    if i==N:
        print(arr)
        return
    arr[i]=1
    print_nums(N,arr,i+1)
    arr[i]=2
    print_nums(N,arr,i+1)



if __name__=="__main__":
    N=int(input("Enter the number of digits:"))
    arr=[0]*N
    i=0
    print_nums(N,arr,i)