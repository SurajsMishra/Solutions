1class Solution:
2    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
3        total_time = 0
4        target = tickets[k]
5        for i,count in enumerate(tickets):
6            if i<= k:
7                total_time += min(count, target)
8            else:
9                total_time += min(count, target - 1)
10        return total_time