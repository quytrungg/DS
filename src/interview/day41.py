import collections

def groupAnagramWords(strs):
    if not strs:
        return
    idx = 0
    result = []
    result.append([strs[0]])
    return

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]