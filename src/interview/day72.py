def find_continuous_k(list, k):
    result = []
    if k in list:
        return [k]
    return result

print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]