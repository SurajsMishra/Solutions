1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if len(nums) <= 2:
4            return len(nums)
5
6        k=2
7        for i in range(2,len(nums)):
8            if nums[i] != nums[k-2]:
9                nums[k] = nums[i]
10                k += 1
11
12        return k