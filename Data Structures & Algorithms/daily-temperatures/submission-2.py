class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []
        for i, t in enumerate(temps):
            # if the value at current index is > stack[-1] then res[thatIndex] = currInx - valIdx
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append([t, i])
            
        return res