class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            numSum = numbers[l] + numbers[r]
            if(target == numSum):
                break
            if(target < numSum):
                r -= 1
                continue
            if(target > numSum):
                l += 1
                continue
            
        return [l+1, r+1]