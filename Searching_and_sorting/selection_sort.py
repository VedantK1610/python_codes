'''
Sequence: 7, 2, 1, 6

(7, 2, 1, 6) –> (1, 7, 2, 6), In the first traverse it finds the minimum element(i.e., 1) and it is placed at 1st position.

(1, 7, 2, 6) –> (1, 2, 7, 6), In the second traverse it finds the 2nd minimum element(i.e., 2) and it is placed at 2nd position.

(1, 2, 7, 6) –> (1, 2, 6, 7), In the third traverse it finds the next minimum element(i.e., 6) and it is placed at 3rd position.

Time Complexity: O(n2)
Auxiliary Space: O(1)

'''

def selection_sort(arr,size):
    for i in range(size):
        min_index=i
        for j in range(i+1,size):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

arr=[7,2,1,3]
size=len(arr)
print(selection_sort(arr,size))