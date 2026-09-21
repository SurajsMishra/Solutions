1class Solution:
2    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
3        nums.sort()
4        n = len(nums)
5        res = []
6        for i in range(n-3):
7            if i>0 and nums[i] == nums[i-1]:
8                continue
9            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
10                break
11            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1]< target:
12                continue
13            for j in range(i+1, n-2):
14                if j> i+1 and nums[j] == nums[j-1]:
15                    continue
16                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
17                    break
18                if nums[i] + nums[j] + nums[n-2] + nums[n-1]<target:
19                    continue
20
21                left, right = j+1, n-1
22                while left<right:
23                    total = nums[i] + nums[j] + nums[left] + nums[right]
24                    if total == target:
25                        res.append([nums[i], nums[j], nums[left], nums[right]])
26                        left += 1
27                        right -= 1
28                        while left<right and nums[left] == nums[left -1]:
29                            left += 1
30                        while left<right and nums[right] == nums[right+1]:
31                            right -=1
32                    elif total<target:
33                        left += 1
34                    else:
35                        right -=1
36        return res                   