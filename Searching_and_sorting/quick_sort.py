'''
It is a faster and highly efficient sorting algorithm. This algorithm follows the divide and conquer approach.
Divide and conquer is a technique of breaking down the algorithms into subproblems, then solving the subproblems,
and combining the results back together to solve the original problem.

Best Case    => O(n*logn)
Average Case =>	O(n*logn)
Worst Case   =>	O(n2)

Best Case Complexity - In Quicksort, the best-case occurs when the pivot element is the middle element or near
                       to the middle element. The best-case time complexity of quicksort is O(n*logn).
Average Case Complexity - It occurs when the array elements are in jumbled order that is not properly ascending and
                          not properly descending. The average case time complexity of quicksort is O(n*logn).
Worst Case Complexity - In quick sort, worst case occurs when the pivot element is either greatest or smallest element.
                        Suppose, if the pivot element is always the last element of the array, the worst case would occur
                        when the given array is sorted already in ascending or descending order.

Space Complexity  =>	O(n*logn)
'''

def partition(elements,start,end):
    pivot_index=start
    pivot=elements[pivot_index]

    start=pivot_index+1
    end=len(elements)-1
    while start<end:
        while start<len(elements) and pivot>=elements[start]:
            start+=1
        while pivot<elements[end]:
            end-=1

        if start<end:
            elements[start],elements[end]=elements[end],elements[start]

    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]

    return end
def quick_sort(elments,start,end):
    if start<end:
        pi=partition(elements,start,end)
        quick_sort(elements,start,pi-1)
        quick_sort(elements,pi+1,end)

if __name__=="__main__":
    elements=[11,9,29,7,2,15,28]
    quick_sort(elements,0,len(elements)-1)
    print(elements)