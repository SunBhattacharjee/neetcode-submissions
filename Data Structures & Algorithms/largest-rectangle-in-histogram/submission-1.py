class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                I, H = stack.pop()
                maxArea = max(maxArea, H * (i - I))
                start = I
            stack.append((start, h))

        for I, H in stack:
            maxArea = max(maxArea, H * (len(heights) - I))

        return maxArea