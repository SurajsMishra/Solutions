1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3        left, right=0, len(nums)-1
4        while left<=right:
5            mid = (left+right)//2
6            if nums[mid]==target:
7                return mid
8            if nums[left]<= nums[mid]:
9                if nums[left]<= target< nums[mid]:
10                    right = mid-1
11                else:
12                    left = mid+1
13            else:
14                if nums[mid]<target<= nums[right]:
15                    left = mid+1
16                else:
17                    right = mid - 1
18        return -1