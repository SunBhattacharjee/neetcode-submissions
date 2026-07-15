class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        bucket = [[] for i in range (len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, value in count.items():
            bucket[value].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            for c in bucket[i]:
                res.append(c)
                if len(res) == k:
                    return res