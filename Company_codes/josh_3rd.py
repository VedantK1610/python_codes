def fun(s):
    items = [item for item in s.split(',')]
    count = 0

    for i in range(len(items) - 3):
        for j in range(i + 1, i + 4):
            if items[i][0] == items[j][0]:
                if items[i][1] == 'B' and items[j][1] == 'C':
                    count += 1
                elif items[i][1] == 'C' and items[j][1] == 'B':
                    count += 1
                else:
                    continue

    return count


s = "8B,9C,3B,8C,9B,4C,4B,3C,1B"
res = fun(s)
print(res)