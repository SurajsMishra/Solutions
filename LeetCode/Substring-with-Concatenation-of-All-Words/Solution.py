1class Solution:
2    def findSubstring(self, s: str, words: List[str]) -> List[int]:
3        if not s or not words:
4            return[]
5        word_len = len(words[0])
6        num_words = len(words)
7        total_len = word_len * num_words
8        s_len = len(s)
9        if s_len < total_len:
10            return []
11
12        word_count = Counter(words)
13        result = []
14        for i in range(word_len):
15            left = i
16            right= i
17            seen = Counter()
18            count =0 
19            while right+word_len <= s_len:
20                word = s[right: right+word_len]
21                right += word_len
22                if word in word_count:
23                    seen[word] += 1
24                    count += 1
25
26                    while seen[word]> word_count[word]:
27                        left_word = s[left: left+word_len]
28                        seen[left_word] -= 1
29                        count -= 1
30                        left += word_len
31
32                    if count == num_words:
33                        result.append(left)
34                else:
35                    seen.clear()
36                    count = 0
37                    left = right
38        return result