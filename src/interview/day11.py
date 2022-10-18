#question: given grid size m and n, return number of ways to get from top-left to bottom-right

def num_ways(n, m):
    if n == 1 and m == 1:
        return 1
    elif n < 1 or m < 1:
        return 0
    return num_ways(n - 1, m) + num_ways(n, m - 1)

print(num_ways(3, 3))
# 2