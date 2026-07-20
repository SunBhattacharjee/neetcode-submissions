class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            # ([{}])
            if c not in matches:
                stack.append(c)
                continue
            if stack and (matches[c] == stack[-1]):
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False
