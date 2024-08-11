def maxSubArraySum(a, size):
    max_so_far = float('-inf')
    curr_max = 0
    start = 0
    end = 0
    temp_start = 0

    for i in range(size):
        curr_max += a[i]

        if max_so_far < curr_max:
            max_so_far = curr_max
            start = temp_start
            end = i

        if curr_max < 0:
            curr_max = 0
            temp_start = i + 1

    return a[start:end + 1]


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Elements of maximum contiguous subarray:", maxSubArraySum(a, len(a)))
