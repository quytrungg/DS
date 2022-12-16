class Solution(object):
  def topKFrequent(self, words, k):
    count = {}
    for i in words:
        try:
            count[i] += 1
        except:
            count[i] = 1
    return list(reversed(dict(sorted(count.items(), key=lambda item: item[1])).keys()))[0:k]

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']