def combinations(ind, n):
    if ind == 0 or n == 0:
        return 1  # Base case: 0 choose anything is 1
    not_pick = combinations(ind - 1, n)
    pick = combinations(ind, n - 1)
    return pick + not_pick

print(combinations(3, 3))  # Output should be 3
