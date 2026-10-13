1class Solution:
2    def missingNumber(self, nums: list[int]) -> int:
3        n= len(nums)
4        expected_sum = n*(n+1)//2
5        actual_sum = sum(nums)
6        return expected_sum - actual_sum