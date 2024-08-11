'''
Time Complexity: O(log n)

Auxiliary Space: O(logn)

'''

# def binary_search(arr,low,high,value):
#     mid=(low+high)//2
#     if high>=low:
#         if arr[mid]==value:
#             return mid
#         if arr[mid]<value:
#             return binary_search(arr,mid+1,high,value)
#         else:
#             return binary_search(arr, low, mid-1, value)
#     else:
#         return -1

def binary_search(arr,low,high,value):
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==value:
            return mid
        elif arr[mid]>value:
            high=mid-1
        else :
            low=mid+1
    return -1


arr=[2,3,5,6,7]
value=6
print(binary_search(arr,0,len(arr)-1,value))