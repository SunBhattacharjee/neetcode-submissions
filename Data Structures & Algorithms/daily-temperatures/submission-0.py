class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res[i] == 2 means that after 2 days from the ith day, the temp will increase
        stack = [] # [t, i]
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res

