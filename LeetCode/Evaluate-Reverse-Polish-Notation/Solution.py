1class Solution:
2    def evalRPN(self, tokens: list[str]) -> int:
3        stack = []
4        for token in tokens:
5            if token == "+":
6                stack.append(stack.pop()+stack.pop())
7            elif token == "-":
8                b=stack.pop()
9                a=stack.pop()
10                stack.append(a-b)
11            elif token == "*":
12                stack.append(stack.pop()*stack.pop())
13            elif token == "/":
14                b=stack.pop()
15                a=stack.pop()
16                stack.append(int(a/b))
17            else:
18                stack.append(int(token))
19
20        return stack.pop()