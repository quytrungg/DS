class Solution: 
    def getRange(self, arr, target):
        range = []
        
        for idx, num in enumerate(arr):
            if num == target:
                range.append(idx)
                
        return [range[0], range[-1]]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]