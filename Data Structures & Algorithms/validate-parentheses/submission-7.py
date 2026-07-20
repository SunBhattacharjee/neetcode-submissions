class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            # ([{}])
            if stack:
                if not matches[c] == stack[-1]:
                    return False
                elif matches[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
        
        if not stack:
            return True
        else:
            return False
