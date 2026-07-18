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
                val = stack.pop()
                if not c == matches[val]:
                    return False

        return True
        