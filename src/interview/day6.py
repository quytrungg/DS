# question: given 2 strings, return steps to make str 1 become str 2

from calendar import c


def distance(s1, s2):
    return editDistance(s1, s2[::-1], len(s1), len(s2))

def editDistance(str1, str2, m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    return editDistance(str1, str2, m-1, n-1) if str1[m-1] == str2[n-1] else 1 + min(editDistance(str1, str2, m, n-1),
                                                                                    editDistance(str1, str2, m-1, n),
                                                                                    editDistance(str1, str2, m-1, n-1))         

print(distance('car', 'racecar'))
# 2