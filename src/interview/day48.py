def longest_subseq(arr):
    if not arr:
        return []
    result = []
    max = []
    for i in range(len(arr)-1):
        start = i
        for j in range(i+1, len(arr)):
            result.append(arr[start])
            end = j 
            while end < len(arr):
                if arr[end] > arr[start]:
                    result.append(arr[end])
                    start = end
                end += 1
            print(result)
            if len(result) > len(max):
                max = result
            result = []
    return max


print(longest_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
# [0, 2, 6, 9 , 11, 15]