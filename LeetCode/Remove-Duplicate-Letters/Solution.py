1class Solution:
2    def removeDuplicateLetters(self, s: str) -> str:
3        last_index = {char: i for i, char in enumerate(s)}
4        stack = []
5        seen = set()
6        for i, char in enumerate(s):
7            if char in seen:
8                continue
9            while stack and stack[-1]>char and last_index[stack[-1]]>i:
10                removed = stack.pop()
11                seen.remove(removed)
12            stack.append(char)
13            seen.add(char)
14        return "".join(stack)