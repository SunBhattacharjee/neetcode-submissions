class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]
        for k, v in count.items():
            freq[v].append(k)

        for i in range(len(nums), 0, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res