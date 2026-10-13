1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        count = 0
4        while n:
5            n &= (n-1)
6            count += 1
7        return count