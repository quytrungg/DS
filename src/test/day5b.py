class Solution: #O(n^3)- Solution: Brute Force
    def longestPalindrome(self, s):
        pld = []
        length = []
        
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                ss = s[i:j]
                flag = 0
                
                for k in range(len(ss)//2):
                    if ss[k] != ss[- k - 1]:
                        flag = 1
                if flag == 0:
                    pld.append(ss)
                    length.append(len(ss))
                    
        return pld[length.index(max(length))]
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar