1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        current_number=0
5        last_op = '+'
6        operators = {'+', '-', '*', '/'}
7        for i, ch in enumerate(s):
8            if ch.isdigit():
9                current_number = current_number*10 + int(ch)
10            if (ch in operators) or (i==len(s) -1):
11                if ch == ' ' and i != len(s) - 1:
12                    continue
13
14                if last_op == '+':
15                    stack.append(current_number)
16                elif last_op == '-':
17                    stack.append(-current_number)
18                elif last_op == '*':
19                    stack.append(stack.pop()*current_number)
20                elif last_op == '/':
21                    stack.append(int(stack.pop()/ current_number))
22                last_op = ch
23                current_number=0
24
25        return sum(stack)