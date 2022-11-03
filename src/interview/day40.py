def count_invalid_parenthesis(string):
    count = 0
    for i in range(len(string)-1):
        if string[i+1] == string[i]:
            count += 1
    return count

print(count_invalid_parenthesis("()())()"))
# 1