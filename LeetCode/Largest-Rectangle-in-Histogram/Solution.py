1class Solution:
2    def largestRectangleArea(self, heights: list[int]) -> int:
3        max_area = 0
4        stack = []
5        heights.append(0)
6        for i, h in enumerate(heights):
7            while stack and heights[stack[-1]]>h:
8                height_idx = stack.pop()
9                height = heights[height_idx]
10                width = i if not stack else i-stack[-1]-1
11                max_area = max(max_area, height*width)
12
13            stack.append(i)
14        return max_area