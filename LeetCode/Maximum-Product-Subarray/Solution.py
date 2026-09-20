1class Solution:
2    def maxProduct(self, nums: list[int]) -> int:
3        res = max(nums)
4        cur_min, cur_max = 1,1
5        for n in nums:
6            if n==0:
7                cur_min, cur_max = 1,1
8                continue
9
10            temp = cur_max * n
11            cur_max = max(n* cur_max, n* cur_min, n)
12            cur_min = min(temp, n* cur_min, n)
13            res = max(res, cur_max)
14
15        return res