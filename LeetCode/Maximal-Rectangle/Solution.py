1class Solution:
2    def maximalRectangle(self, matrix: list[list[str]]) -> int:
3        if not matrix or not matrix[0]:
4            return 0
5        cols = len(matrix[0])
6        heights = [0]*cols
7        max_area=0
8        for row in matrix:
9            for j in range(cols):
10                heights[j] = heights[j] + 1 if row[j] == '1' else 0
11
12            stack = []
13            for i,h in enumerate(heights + [0]):
14                while stack and heights[stack[-1]]>h:
15                    height = heights[stack.pop()]
16                    width = i if not stack else i -stack[-1] -1
17                    max_area = max(max_area, height*width)
18                stack.append(i)
19        return max_area