1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        max_sum = nums[0]
4        current_sum = nums[0]
5        for num in nums[1:]:
6            current_sum = max(num, current_sum+num)
7            max_sum = max(max_sum, current_sum)
8
9        return max_sum