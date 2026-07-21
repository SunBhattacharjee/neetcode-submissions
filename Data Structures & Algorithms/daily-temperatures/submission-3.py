class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)

        return result
