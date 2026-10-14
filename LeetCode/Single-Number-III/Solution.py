1class Solution:
2    def singleNumber(self, nums: list[int]) -> list[int]:
3        xor_sum = 0
4        for num in nums:
5            xor_sum ^= num
6        diff_bit = xor_sum & (-xor_sum)
7        num1, num2 = 0,0
8        for num in nums:
9            if num & diff_bit:
10                num1 ^= num
11            else:
12                num2 ^= num
13
14        return [num1,num2]