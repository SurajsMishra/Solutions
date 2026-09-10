1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if not s or not t or len(s) < len(t):
4            return ""
5        need = Counter(t)
6        required = len(need)
7        have = {}
8        formed = 0
9        ans = (float("inf"), None, None)
10        left = 0
11        for right, char in enumerate(s):
12            have[char] = have.get(char,0)+1
13            if char in need and have[char] == need[char]:
14                formed += 1
15            while formed == required:
16                if right - left + 1 < ans[0]:
17                    ans = (right - left +1, left, right)
18
19                left_char = s[left]
20                have[left_char] -= 1
21                if left_char in need and have[left_char] < need[left_char]:
22                    formed -= 1
23                left += 1
24
25        return "" if ans[0] == float("inf") else s[ans[1] : ans[2]+1]