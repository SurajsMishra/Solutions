1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        i = len(s)-1
4        j = len(t)-1
5        
6        while (i>=0 or j>=0):
7            skip_s=0
8            while i>=0:
9                if s[i] =='#':
10                    skip_s += 1
11                    i -= 1
12                elif skip_s >0:
13                    skip_s -= 1
14                    i -= 1
15                else:
16                    break
17            skip_t=0
18            while j>=0:
19                if t[j]=='#':
20                    skip_t += 1
21                    j -=1
22                elif skip_t >0:
23                    skip_t -= 1
24                    j -= 1
25                else:
26                    break
27            if i>= 0 and j>= 0 and s[i] != t[j]:
28                return False
29            if (i>= 0) != (j>=0):
30                return False
31            i -= 1
32            j -= 1
33        return True