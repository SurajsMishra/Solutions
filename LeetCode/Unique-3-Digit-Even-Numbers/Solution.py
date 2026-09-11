1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        count = 0
4        digit_counts = Counter(digits)
5        for num in range(100, 1000, 2):
6            d1 = num//100
7            d2 = (num // 10)% 10
8            d3 = num  % 10
9
10            req = Counter([d1,d2,d3])
11            if all(digit_counts[d] >= req[d] for d in req):
12                count += 1
13
14        return count