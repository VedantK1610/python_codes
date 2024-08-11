'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import numpy as np


def getFirst(arr, low, high):
    if high >= low:
        mid = low + (high - low) // 2

        if (arr[mid] == 1 and (arr[mid - 1] == 0 or mid == 0)):
            return mid
        elif arr[mid] == 0:
            return getFirst(arr, mid + 1, high)
        else:
            return getFirst(arr, low, mid - 1)


    return -1


def maxCount(mat, r, c):
    m = -1
    res = 0
    for i in range(r):
        index = getFirst(mat[i], 0, c - 1)
        if (index != -1 and c - index > m):
            m = c - index
            res = i

    return res


mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

a = np.array(mat)
r, c = a.shape
print(maxCount(mat, r, c))
