class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s) % 2 == 0:
            return False
        matches = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in matches:
                stack.append(c)
            else:
                peek = stack[-1]
                if not c == matches[peek]:
                    break
                else:
                    stack.pop()

        return True if len(stack) == 0 else False
        