def get_maximum_expertise(n, c, conflicts, expertise):
    conflict_masks = [0] * n
    for a, b in conflicts:
        conflict_masks[a - 1] |= 1 << (b - 1)
        conflict_masks[b - 1] |= 1 << (a - 1)

    maximum_expertise = [-1] * (1 << n)
    maximum_expertise[0] = 0

    for mask in range(1, 1 << n):
        for employee in range(n):
            if mask & (1 << employee) == 0 and (mask & conflict_masks[employee]) == 0:
                maximum_expertise[mask | (1 << employee)] = max(maximum_expertise[mask | (1 << employee)],
                                                               maximum_expertise[mask] + expertise[employee])

    return max(maximum_expertise)


n, c = map(int, input().split())
conflicts = []
for _ in range(c):
    a, b = map(int, input().split())
    conflicts.append((a, b))

expertise = list(map(int, input().split()))

print(get_maximum_expertise(n, c, conflicts, expertise))
