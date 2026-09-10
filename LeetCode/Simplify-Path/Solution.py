1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack = []
4        components = path.split("/")
5        for part in components:
6            if part == "" or part == ".":
7                continue
8            elif part == "..":
9                if stack:
10                    stack.pop()
11            else:
12                stack.append(part)
13
14        return "/" + "/".join(stack)