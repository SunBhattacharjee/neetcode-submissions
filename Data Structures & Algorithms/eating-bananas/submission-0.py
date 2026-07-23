class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        i = 0
        while l <= r:
            k = (l + r) // 2
            time = 0
            for c in piles:
                time += math.ceil(c/k)
            if time <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res