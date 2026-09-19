1class Solution {
2    public boolean checkSubarraySum(int[] nums, int k) {
3        Map<Integer, Integer> remainderMap = new HashMap<>();
4        remainderMap.put(0,-1);
5        int runningSum = 0;
6        for(int i=0; i<nums.length; i++){
7            runningSum += nums[i];
8            int remainder = runningSum % k;
9            if(remainderMap.containsKey(remainder)){
10                if(i-remainderMap.get(remainder)>=2){
11                    return true;
12                }
13            }else{
14                remainderMap.put(remainder, i);
15            }
16        }
17        return false; 
18    }
19}