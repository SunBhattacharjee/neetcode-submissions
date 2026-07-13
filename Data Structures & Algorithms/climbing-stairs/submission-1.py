class Solution:
    def climbStairs(self, n: int) -> int:
        prev2, prev1 = 0, 1
        for i in range(1, n+1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        return prev1


        # 0 1 2
        
