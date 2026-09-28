1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        if not matrix or not matrix[0]:
4            return False
5        rows, cols = len(matrix), len(matrix[0])
6        row, col = 0, cols-1
7        while row<rows and col>=0:
8            current = matrix[row][col]
9            if current == target:
10                return True
11            elif current>target:
12                col -= 1
13            else:
14                row += 1
15        return False