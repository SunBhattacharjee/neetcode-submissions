class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0] * n
        stack = []
        for i, t in enumerate(temps):
            while stack and t > temps[stack[-1]]:
                stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append(i)
        return res