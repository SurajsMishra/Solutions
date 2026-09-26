1class Solution:
2    def rotate(self, nums: list[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n = len(nums)
7        k %=n
8
9        def reverse(start: int , end:int) -> None:
10            while start<end:
11                nums[start], nums[end] = nums[end], nums[start]
12                start += 1
13                end -= 1
14            
15        reverse(0, n-1)
16        reverse(0, k-1)
17        reverse(k, n-1)