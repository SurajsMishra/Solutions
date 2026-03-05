class Solution {
    public int minOperations(String s) {
        int n = s.length();
        int pattern1 = 0;
        int pattern2 = 0;
        for(int i = 0; i < n; i++){
            char excepted1 = (i % 2 == 0) ? '0' : '1';
            char excepted2 = (i % 2 == 0) ? '1' : '0';
            if(s.charAt(i) != excepted1){
                pattern1++;
            }
            if(s.charAt(i) != excepted2){
                pattern2++;
            }
            
        }
        return Math.min(pattern1 , pattern2);
    }
}