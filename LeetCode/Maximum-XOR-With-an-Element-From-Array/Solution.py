1class TrieNode:
2    def __init__(self):
3        self.children = {}
4class Trie:
5    def __init__(self):
6        self.root = TrieNode()
7    def insert(self,num):
8        node = self.root
9        for i in range(31,-1,-1):
10            bit = (num>>i)&1
11            if bit not in node.children:
12                node.children[bit] = TrieNode()
13            node = node.children[bit]
14    def get_max_xor(self,num):
15        node = self.root
16        if not node.children:
17            return -1
18
19        max_xor = 0
20        for i in range(31,-1,-1):
21            bit = (num>>i)&1
22            target_bit = 1-bit
23            if target_bit in node.children:
24                max_xor |= (1<<i)
25                node = node.children[target_bit]
26            elif bit in node.children:
27                node = node.children[bit]
28            else:
29                break
30        return max_xor
31
32class Solution:
33    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
34        nums.sort()
35        indexed_queries = [(x,m,i) for i, (x,m) in enumerate(queries)]
36        indexed_queries.sort(key=lambda q: q[1])
37        ans = [-1] * len(queries)
38        trie = Trie()
39        nums_idx = 0
40        n = len(nums)
41        for x,m,original_idx in indexed_queries:
42            while nums_idx < n and nums[nums_idx]<= m:
43                trie.insert(nums[nums_idx])
44                nums_idx += 1
45            if nums_idx == 0:
46                ans[original_idx] = -1
47            else:
48                ans[original_idx] = trie.get_max_xor(x)
49        return ans        