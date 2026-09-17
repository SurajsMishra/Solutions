1from collections import defaultdict
2class Solution:
3    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
4        def atMostK(k: int) -> int:
5            count = defaultdict(int)
6            left = 0
7            total_subarrays = 0
8            for right in range(len(nums)):
9                if count[nums[right]] == 0:
10                    k -= 1
11                count[nums[right]] += 1
12                while k<0:
13                    count[nums[left]] -= 1
14                    if count[nums[left]] == 0:
15                        k += 1
16                    left += 1
17                total_subarrays += right-left + 1
18            return total_subarrays
19
20        return atMostK(k) - atMostK(k-1)