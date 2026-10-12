1class Solution:
2    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        res = []
5        def backtrack(start: int, path: list[int]):
6            res.append(path.copy())
7            for i in range(start, len(nums)):
8                if i>start and nums[i]==nums[i-1]:
9                    continue
10                path.append(nums[i])
11                backtrack(i+1, path)
12                path.pop()
13
14        backtrack(0, [])
15        return res
16
17            