def two_sum(list, k): #find if there is at least a pair of number
    remain = []
    for idx, num in enumerate(list):
        if num in remain:
            return True
        remain.append(num - k)
    return False

print(two_sum([4,7,1,-3,2], 5))
# True