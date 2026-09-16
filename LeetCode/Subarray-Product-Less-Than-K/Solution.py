1class Solution:
2    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
3        if k <= 1:
4            return 0
5        prod = 1
6        ans = 0
7        left = 0
8        for right in range(len(nums)):
9            prod *= nums[right]
10
11            while prod >= k:
12                prod //= nums[left]
13                left += 1
14
15            ans += right - left + 1
16
17        return ans