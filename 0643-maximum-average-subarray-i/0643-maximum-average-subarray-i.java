class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        
        // 1. Sum the first window
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        
        int maxSum = sum;
        
        // 2. Slide the window from index k to the end of the array
        for (int i = k; i < nums.length; i++) {
            sum = sum - nums[i - k] + nums[i];
            maxSum = Math.max(maxSum, sum);
        }
        
        return (double) maxSum / k;
    }
}