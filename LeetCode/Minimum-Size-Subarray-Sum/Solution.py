1class Solution:
2    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
3        left = 0
4        current_sum = 0
5        min_len = float('inf')
6        for right in range(len(nums)):
7            current_sum += nums[right]
8            while current_sum >= target:
9                min_len = min(min_len, right-left + 1)
10                current_sum -= nums[left]
11                left += 1
12        return min_len if min_len != float('inf') else 0