class Solution:
    def numDecodings(self, s: str) -> int:
        def f(i, s):
            if len(s) == 0:
                return 0
            if len(s) == 1 and s[0] == '0':
                return 0
            pick_one = f(i+1, s[i+1:])
            pick_two = 0
            if int(s[:i+2]) < 27:
                pick_two = f(i+2, s[i+2:])
            return 1 + (pick_one + pick_two)

        if s[0] == '0':
            return 0
        return f(0, s)
        

        