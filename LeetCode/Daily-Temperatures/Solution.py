1class Solution:
2    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
3        n = len(temperatures)
4        answer = [0]*n
5        stack=[]
6        for i in range(n):
7            while stack and temperatures[i]>temperatures[stack[-1]]:
8                prev_day = stack.pop()
9                answer[prev_day] = i - prev_day
10            stack.append(i)
11        return answer