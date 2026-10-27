class Solution {
    public boolean isPalindrome(int x) {
        int original = x;
        int pal = 0;
        while(x > 0){
            int rem = x %10;
            pal = pal*10 + rem;
            x = x/10;
        }
        if(original == pal){
            return true;
        }else{
            return false;
        }
    }
}