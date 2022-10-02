# question: given a string of '.', 'R', 'L', create domino string

class Solution(object):
    def pushDominoes(self, dominoes):
        list = []
        list[:0] = dominoes
        for i in range(len(list) - 1):
            if list[i] == 'R':
                j = i + 1
                if list[j] == '.' and list[j+1] != 'L':
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
                    else:
                        for k in range(i, j+1):
                            list[k] = 'R'
        return ''.join(list)

print(Solution().pushDominoes('..R.......L..R.......L.'))
# ..RR.LL..RR