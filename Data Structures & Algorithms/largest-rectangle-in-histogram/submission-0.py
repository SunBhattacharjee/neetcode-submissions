class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            stack.append(i)
            width = 1
            while stack and heights[stack[-1]] > heights[i]:
                width += 1
                stack.pop()
            maxArea = max(maxArea, (width * heights[i]))
        return maxArea