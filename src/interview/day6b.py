class Solution: #using stack
    def isValid(self, s):
        if len(s) == 0:
            return True
        
        _open = ['(', '[', '{']
        _close = [')', ']', '}']
        
        stack = []
        
        for i in range(len(s)):
            if s[i] in _open:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                
                cur = stack.pop()
                
                if s[i] != _close[_open.index(cur)]:
                    return False
                    
        if stack:
            return False
        return True
        
        
# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))