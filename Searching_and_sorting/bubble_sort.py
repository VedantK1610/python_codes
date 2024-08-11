''' Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
     if they are in the wrong order.This algorithm is not suitable for large data sets as its average
     and worst-case time complexity is quite high.

     Time Complexity: O(N**2)
     Auxiliary Space: O(1)

    Bubble sort takes minimum time (O(n)) when elements are already sorted.
'''

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(0,len(arr)-i-1): #as we are placing largest element at end of array during each loop so n-i-1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:  #if nothing swapped,all elements are already sorted no need to loop again
            break

if __name__=="__main__":
    arr=[2,1,3,4,0]
    bubble_sort(arr)
    print(arr)
