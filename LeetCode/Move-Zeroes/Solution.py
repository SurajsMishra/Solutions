1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n =0 
7        for i in range(len(nums)):
8            if(nums[i] != 0):
9                nums[n], nums[i] = nums[i], nums[n]
10                n += 1