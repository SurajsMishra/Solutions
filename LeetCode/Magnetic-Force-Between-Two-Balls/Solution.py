1class Solution:
2    def maxDistance(self, position: list[int], m: int) -> int:
3        position.sort()
4
5        def canPlace(force: int) -> bool:
6            count = 1
7            last_pos = position[0]
8            for i in range(1, len(position)):
9                if position[i] - last_pos >= force:
10                    count += 1
11                    last_pos = position[i]
12                    if count >= m:
13                        return True
14            
15            return False
16
17        low, high = 1, (position[-1] - position[0]) // (m-1)
18        ans =1
19        while low<= high:
20            mid = (low+high)//2
21            if canPlace(mid):
22                ans = mid
23                low = mid+1
24            else:
25                high = mid -1
26        return ans