1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        return n>0 and (n&(n-1)) == 0