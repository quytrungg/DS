def findTime(arr, cooldown):
    count = 0
    temp = []
    for i in range(len(arr) - 1):
        if temp == []:
            temp.append(arr[i])
        count += 1
        if arr[i+1] in temp:
            count += 2
        else:
            count += 1
    return count

print(findTime([1, 1, 2, 1], 2))
# 7