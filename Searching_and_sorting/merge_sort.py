'''
1. write logic for merge_arrays
2.then go for merge_sort

Time Complexity: O(n*log(n))
Auxilary Space : O(n)

logic is to divide the array in two subarrays. Follow this dividation until it becomes array of 1 element then merge
the arrays.
'''

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge_arrays(left,right)

def merge_arrays(a,b):
    sorted_list=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i<len(a):
        sorted_list.append(a[i])
        i+=1
    while j<len(b):
        sorted_list.append(b[j])
        j+=1
    return sorted_list

arr=[10,2,7,8,1,3]
print(merge_sort(arr))