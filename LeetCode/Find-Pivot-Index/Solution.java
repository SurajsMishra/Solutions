1class Solution {
2    public int pivotIndex(int[] nums) {
3        int totalSum = 0;
4        for(int num: nums){
5            totalSum += num;
6        }
7        int leftSum = 0;
8        for(int i =0; i<nums.length; i++){
9            if(leftSum == totalSum - leftSum - nums[i]){
10                return i;
11            }
12            leftSum += nums[i];
13        }
14        return -1;
15    }
16}