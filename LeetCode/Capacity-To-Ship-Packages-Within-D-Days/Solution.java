1class Solution {
2    public int shipWithinDays(int[] weights, int days) {
3        int low = 0;
4        int high = 0;
5        for(int w: weights){
6            low = Math.max(low, w);
7            high += w;
8        }
9        int ans = high;
10        while(low<=high){
11            int mid = low+(high-low)/2;
12            if(canShip(weights, days, mid)){
13                ans = mid;
14                high = mid-1;
15            }else{
16                low = mid+1;
17            }
18        }
19        return ans;
20    }
21    private boolean canShip(int [] weights, int days, int capacity){
22        int neededDays = 1;
23        int currentWeight = 0;
24        for(int w: weights){
25            if(currentWeight + w > capacity){
26                neededDays++;
27                currentWeight = 0;
28            }
29            currentWeight += w;
30        }
31        return neededDays <= days;
32    }
33}