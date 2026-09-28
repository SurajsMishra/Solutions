1class Solution:
2    def splitArray(self, nums: list[int], k: int) -> int:
3        def can_split(max_sum_limit: int) -> bool:
4            count =1
5            current_sum = 0
6            for num in nums:
7                if current_sum + num > max_sum_limit:
8                    count += 1
9                    current_sum = num
10                else:
11                    current_sum += num
12
13            return count<= k
14        low = max(nums)
15        high = sum(nums)
16        ans = high
17        while low<=high:
18            mid = (low+high)//2
19            if can_split(mid):
20                ans = mid
21                high = mid-1
22            else:
23                low = mid+1
24
25        return ans
26
27       