# question: given array, count witnesses, k-1 > k

def witnesses(heights):
    min = 0
    count = 0
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > min:
            min = heights[i]
            count += 1
    return count

print(witnesses([3, 6, 3, 4, 1]))
# 3