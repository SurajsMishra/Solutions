1class Solution:
2    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
3        next_greater={}
4        stack = []
5        for num in nums2:
6            while stack and num>stack[-1]:
7                next_greater[stack.pop()]= num
8            stack.append(num)
9
10        return [next_greater.get(x,-1) for x in nums1]
11        