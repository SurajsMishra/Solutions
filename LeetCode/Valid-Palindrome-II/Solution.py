1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        def is_palindrome(left:int, right: int) -> bool:
4            while left<right:
5                if s[left] != s[right]:
6                    return False
7                left += 1
8                right -=1
9            return True
10
11        left, right =0, len(s)-1
12        while left<right:
13            if s[left] != s[right]:
14                return is_palindrome(left+1, right) or is_palindrome(left, right-1)
15            left += 1
16            right -= 1
17        return True