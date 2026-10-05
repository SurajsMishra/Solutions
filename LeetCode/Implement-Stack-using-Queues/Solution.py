1class MyStack:
2
3    def __init__(self):
4        self.q = deque()
5
6    def push(self, x: int) -> None:
7        self.q.append(x)
8        for i in range(len(self.q)-1):
9            self.q.append(self.q.popleft())
10
11    def pop(self) -> int:
12        return self.q.popleft()
13
14    def top(self) -> int:
15        return self.q[0]
16
17    def empty(self) -> bool:
18        return len(self.q)==0
19
20
21# Your MyStack object will be instantiated and called as such:
22# obj = MyStack()
23# obj.push(x)
24# param_2 = obj.pop()
25# param_3 = obj.top()
26# param_4 = obj.empty()