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
                if stack:
                    val = stack.pop()
                    if not c == matches[val]:
                        break

        return True if len(stack) == 0 else False
        