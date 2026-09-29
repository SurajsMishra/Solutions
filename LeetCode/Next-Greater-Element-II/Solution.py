1class Solution:
2    def nextGreaterElements(self, nums: list[int]) -> list[int]:
3        n=len(nums)
4        res = [-1]*n
5        stack = []
6        for i in range(2*n):
7            idx = i%n
8            while stack and nums[stack[-1]]<nums[idx]:
9                prev_idx = stack.pop()
10                res[prev_idx] = nums[idx]
11
12            if i<n:
13                stack.append(idx)
14        return res