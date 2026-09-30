1class Solution:
2    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
3        if len(nums1) > len(nums2):
4            nums1, nums2 = nums2, nums1
5        m,n = len(nums1), len(nums2)
6        low, high = 0, m
7        total_left = (m+n+1)//2
8        while low<=high:
9            i=(low+high)//2
10            j = total_left-i
11            A_left = nums1[i-1] if i>0 else float("-inf")
12            A_right = nums1[i] if i<m else float("inf")
13            B_left = nums2[j-1] if j>0 else float("-inf")
14            B_right = nums2[j] if j<n else float("inf")
15            if A_left <= B_right and B_left <= A_right:
16                if(m+n)%2 == 1:
17                    return float(max(A_left, B_left))
18                return (max(A_left, B_left)+ min(A_right, B_right)) / 2.0
19            elif A_left>B_right:
20                high = i-1
21            else:
22                low = i+1
23        return 0.0