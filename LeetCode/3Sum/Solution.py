1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        new = []
4        nums.sort()
5        n = len(nums)
6        for i in range(n-2):
7            if nums[i] >0:
8                break
9            if i>0 and nums[i] == nums[i-1]:
10                continue
11
12            left, right = i+1, n-1
13            while left<right:
14                total = nums[i] + nums[left] + nums[right]
15                if total == 0:
16                    new.append([nums[i], nums[left], nums[right]])
17                    left += 1
18                    right -= 1
19
20                    while left<right and nums[left] == nums[left -1]:
21                        left += 1
22
23                    while left<right and nums[right] == nums[right + 1]:
24                        right -= 1
25
26                elif total < 0:
27                    left += 1
28
29                else:
30                    right -= 1
31
32        return new