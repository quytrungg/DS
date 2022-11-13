def reverse(x):
    if int(x) >= 2**31:
        return 0
    return int(str(x)[::-1])

print(reverse(123))
# 321
print(reverse(2**31))
# 0