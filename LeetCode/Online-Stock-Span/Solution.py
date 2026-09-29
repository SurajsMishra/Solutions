1class StockSpanner:
2
3    def __init__(self):
4        self.stack = []
5
6    def next(self, price: int) -> int:
7        span = 1
8        while self.stack and self.stack[-1][0]<=price:
9            span += self.stack.pop()[-1]
10        self.stack.append((price,span))
11        return span
12
13
14# Your StockSpanner object will be instantiated and called as such:
15# obj = StockSpanner()
16# param_1 = obj.next(price)