def fix_brackets(s):
    left = 0
    right = 0
    for i in s:
        if i == '(':
            left += 1
        else:
            right += 1
    if left > right:
        return left - right
    else:
        return right - left

print(fix_brackets('(()()'))
# 1