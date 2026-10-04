1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.min_stack = []
6
7    def push(self, value: int) -> None:
8        self.stack.append(value)
9        if not self.min_stack or value <= self.min_stack[-1]:
10            self.min_stack.append(value)
11
12    def pop(self) -> None:
13        if self.stack:
14            value = self.stack.pop()
15            if value == self.min_stack[-1]:
16                self.min_stack.pop()
17
18    def top(self) -> int:
19        return self.stack[-1]
20
21    def getMin(self) -> int:
22        return self.min_stack[-1]
23
24
25# Your MinStack object will be instantiated and called as such:
26# obj = MinStack()
27# obj.push(value)
28# obj.pop()
29# param_3 = obj.top()
30# param_4 = obj.getMin()