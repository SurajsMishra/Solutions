1class Solution:
2    def subarraysDivByK(self, nums: list[int], k: int) -> int:
3        remainder_count = {0: 1}
4        prefix_sum = 0
5        count = 0
6        for num in nums:
7            prefix_sum += num
8            remainder = prefix_sum % k
9            if remainder in remainder_count:
10                count += remainder_count[remainder]
11                remainder_count[remainder] += 1
12            else:
13                remainder_count[remainder] = 1
14
15        return count