# question: given a string of '.', 'R', 'L', create domino string

class Solution(object):
    def pushDominoes(self, dominoes):
        list = []
        list[:0] = dominoes
        for i in range(len(list) - 1):
            if list[i] == 'R':
                j = i + 1
                while list[j] != 'L' and j+1 < len(list):
                    j += 1
                if(list[j] == 'L'):
                    left = i + 1
                    right = j - 1
                    while left < right:
                        list[left] = 'R'
                        list[right] = 'L'  
                        left += 1
                        right -= 1
                else: list[j] = 'R'
        return ''.join(list)

print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR