class Solution {
    public int[] runningSum(int[] nums) {
        int[] arr = new int[nums.length];
        int value = 0;
        int i = 0;
        while(i< nums.length){
            value += nums[i];
            arr[i] = value;
            i++;
        }
        return arr;
    }
}