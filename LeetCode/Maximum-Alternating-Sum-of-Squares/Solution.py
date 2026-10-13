1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        squared = sorted([x * x for x in nums])
4        n = len(squared)
5        mid = n//2
6        subtractions = squared[:mid]
7        additions = squared[mid:]
8        return sum(additions) - sum(subtractions)