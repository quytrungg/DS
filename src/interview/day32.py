def longest_substring_with_k_distinct_characters(s, k):
    max = 0
    check = []
    for i in range(len(s) - 1):
        end = i + 1
        check.append(s[i])
        while k > 1:
            if s[end] not in check:
                check.append(s[end])
                k -= 1
            end += 1
        max = end - i + 1 if max < end - i + 1 else max

    return max

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)