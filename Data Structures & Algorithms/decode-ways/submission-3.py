class Solution:
    def numDecodings(self, s: str) -> int:
        def f(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            
            pick_one = f(i+1)
            pick_two = 0
            if(i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                pick_two = f(i+2)

            return pick_one + pick_two

        return f(0)
        

        