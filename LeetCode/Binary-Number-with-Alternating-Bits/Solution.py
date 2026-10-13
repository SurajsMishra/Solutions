1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        n = n^(n>>1)
4        return (n&(n+1)) == 0