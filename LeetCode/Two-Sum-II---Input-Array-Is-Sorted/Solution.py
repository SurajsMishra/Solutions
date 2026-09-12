1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        new  =[]
4        n , m = 0, len(numbers)-1
5        while (n<m):
6            if(numbers[n] + numbers[m] == target):
7                return [n+1 , m+1]
8            elif (numbers[n] + numbers[m]) < target:
9                n += 1
10            else:
11                m -=1 
12
13        return []
14