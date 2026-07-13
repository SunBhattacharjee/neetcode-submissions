class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            if value >= k:
                res.append(key)

        return res
        