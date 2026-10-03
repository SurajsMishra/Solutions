1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        mapping = {")":"(","}":"{","]":"["}
5        for char in s:
6            if char in mapping:
7                top_element = stack.pop() if stack else '#'
8                if mapping[char] != top_element:
9                    return False
10            else:
11                stack.append(char)
12        return not stack
13        