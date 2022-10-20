from re import L


def capacity(arr):
    sum = 0
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            continue
        if arr[i] == 0:
            left = i-1
            right = i + 1
            while arr[left] != 0 and arr[right] != 0:
                horizontal = right - left - 1
                vertical = 1
                sum += arr[left] if arr[left] < arr[right] else arr[right]

    return

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6