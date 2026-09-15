1class Solution {
2    public long maximumSubarraySum(int[] nums, int k) {
3        long maxSum = 0;
4        long currentSum = 0;
5        Map<Integer, Integer> countMap = new HashMap<>();
6        for(int i =0; i<nums.length; i++){
7            currentSum += nums[i];
8            countMap.put(nums[i], countMap.getOrDefault(nums[i], 0)+1);
9            if(i>=k){
10                int leftVal = nums[i-k];
11                currentSum -= leftVal;
12                countMap.put(leftVal, countMap.get(leftVal)-1);
13                if(countMap.get(leftVal)==0){
14                    countMap.remove(leftVal);
15                }
16            }
17            if(i>=k-1 && countMap.size() == k){
18                maxSum = Math.max(maxSum, currentSum);
19            }
20        }
21        return maxSum;        
22    }
23}