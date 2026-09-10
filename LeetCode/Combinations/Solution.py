1class Solution:
2    def combine(self, n: int, k: int) -> List[List[int]]:
3        res = []
4        def backtrack(start: int, path: [int]):
5            if len(path) == k:
6                res.append(path[:])
7                return
8
9            need = k -len(path)
10            for i in range(start, n-need + 2):
11                path.append(i)
12                backtrack(i+1, path)
13                path.pop()
14        
15        backtrack(1,[])
16        return res