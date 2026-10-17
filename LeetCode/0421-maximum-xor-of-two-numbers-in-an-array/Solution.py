class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            prefixes = {num & mask for num in nums}
            trial = max_xor | (1<<i)
            found = False
            for p in prefixes:
                if(trial ^ p) in prefixes:
                    found = True
                    break
            if found:
                max_xor = trial
        return max_xor