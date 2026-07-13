import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        ans = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            res.append([-value, key])

        heapq.heapify(res)
        
        for i in range(k):
            iteration, number = heapq.heappop(res)
            ans.append(number)

        return ans
        