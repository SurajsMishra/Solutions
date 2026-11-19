class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int close = nums[0]+ nums[1]+ nums[2]; 
        Arrays.sort(nums);
        int i = 0;
        int n= nums.length;
        int mindiff = Math.abs(close - target);
        for(i=0; i<n-2; i++){
            int left = i+1;
            int right = n-1;
            int sum = -1* nums[i];
              

            while(left<right){
                int s = nums[i] + nums[left] + nums[right];
                int diff = Math.abs(s - target);
                if(diff< mindiff){
                    mindiff = diff;
                    close = s;
                }
                if(s< target){
                    left++;
                }else if(s>target){
                    right--;
                }else{
                    return s;
                }
            }
        }
        return close;
    }
}