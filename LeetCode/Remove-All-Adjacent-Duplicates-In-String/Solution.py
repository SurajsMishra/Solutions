1class Solution:
2    def removeDuplicates(self, s: str) -> str:
3        stack = []
4        for char in s:
5            if stack and stack[-1] == char:
6                stack.pop()
7            else:
8                stack.append(char)
9        return "".join(stack)