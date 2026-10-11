1class Solution:
2    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
3        n = len(arr)
4        pref = [0]*n
5        pref[0] = arr[0]
6        for i in range(1,n):
7            pref[i]=pref[i-1] ^ arr[i]
8        ans = []
9        for left, right in queries:
10            if left == 0:
11                ans.append(pref[right])
12            else:
13                ans.append(pref[right]^pref[left-1])
14        return ans