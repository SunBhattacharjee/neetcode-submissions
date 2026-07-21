class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in match:
                if stack and not match[c] == stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return True if not stack else False
        