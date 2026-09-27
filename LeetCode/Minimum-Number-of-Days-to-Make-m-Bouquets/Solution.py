1class Solution:
2    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
3        if m*k > len(bloomDay):
4            return -1
5        def canMake(day: int) -> bool:
6            bouquets = 0
7            flowers = 0
8            for bloom in bloomDay:
9                if bloom<=day:
10                    flowers += 1
11                    if flowers == k:
12                        bouquets += 1
13                        flowers = 0
14                else:
15                    flowers = 0
16            return bouquets >= m
17
18        low, high = min(bloomDay), max(bloomDay)
19        while low<high:
20            mid = (low+high)//2
21            if canMake(mid):
22                high = mid
23            else:
24                low = mid+1
25
26        return low