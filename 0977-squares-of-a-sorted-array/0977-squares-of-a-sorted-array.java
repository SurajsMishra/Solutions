class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int start =0;
        int end = n-1;
        int i =n-1;
        while(start<=end){
            int lsquare = nums[start] * nums[start];
            int rsquare = nums[end] * nums[end];
            if(lsquare>rsquare){
                result[i] = lsquare;
                start++;
            }else{
                result[i] = rsquare;
                end--;
            }
            i--;
        }
        return result;
    }
}