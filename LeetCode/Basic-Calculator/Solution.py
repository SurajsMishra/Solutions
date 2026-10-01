1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        total = 0
5        current_num=0
6        sign = 1
7        for ch in s:
8            if ch.isdigit():
9                current_num = current_num*10 + int(ch)
10            elif ch in ('+', '-'):
11                total += sign * current_num
12                current_num=0
13                sign = 1 if ch == '+' else -1
14            elif ch == '(':
15                stack.append(total)
16                stack.append(sign)
17                sign = 1
18                total = 0
19            elif ch ==')':
20                total += sign * current_num
21                current_num = 0
22                total *= stack.pop()
23                total += stack.pop()
24        total += sign*current_num
25        return total