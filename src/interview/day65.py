class Solution(object):
  def compress(self, chars):
    count = {}
    result = []
    for i in chars:
        try:
            count[i] += 1
        except:
            count[i] = 1
    for i, j in count.items():
        result.append(i)
        if j > 1:
            result.append(j)
    return result

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']