def products(nums):
    result = []
    for i in range(len(nums)):
        mul = 1
        for j in range(len(nums)):
            if i != j:
                mul *= nums[j]
        result.append(mul)
    return result

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]