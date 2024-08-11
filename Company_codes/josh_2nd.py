
def fun(s):
    heights = [int(i) for i in s.split(',')]
    count = 0
    max_height_index = heights.index(max(heights))

    for i in range(max_height_index):
        if heights[i] > heights[max_height_index]:
            count += 1
        elif heights[i] == heights[i + 1] and i + 1 < max_height_index:
            count += 1
        elif heights[i] > heights[i + 1] and i + 1 < max_height_index:
            count += 1
    for i in range(max_height_index + 1, len(heights)):
        if i == len(heights) - 1:
            if heights[i] > heights[max_height_index]:
                count += 1
            elif heights[i - 1] < heights[i]:
                count += 1
            if count == 0:
                return "NOT POSSIBLE"
            return count
        if heights[i] > heights[max_height_index]:
            count += 1
        elif heights[i] == heights[i + 1]:
            count += 1
        elif heights[i] < heights[i + 1]:
            count += 1


s = '6,2,2,8,6,1,3,2'
res = fun(s)
print(res)