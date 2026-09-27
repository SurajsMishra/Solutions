1class Solution {
2    public int minEatingSpeed(int[] piles, int h) {
3        int left = 1;
4        int right = 0;
5        for(int pile: piles){
6            right = Math.max(right, pile);
7        }
8        int result = right;
9        while(left<=right){
10            int mid = left+(right-left)/2;
11            if(canFinish(piles, h, mid)){
12                result = mid;
13                right = mid -1;
14            }
15            else{
16                left = mid+1;
17            }
18        }
19        return result;
20    }
21    private boolean canFinish(int[] piles, int h, int k){
22        long hours =0 ;
23        for(int pile: piles){
24            hours += (pile+k-1)/k;
25        }
26        return hours <= (long)h;
27    }
28}