1class Solution {
2    public boolean backspaceCompare(String s, String t) {
3        int i = s.length() -1;
4        int j = t.length() -1;
5        int skipS = 0, skipT = 0;
6        while (i>=0 || j>=0){
7            while(i>=0){
8                if(s.charAt(i) == '#'){
9                    skipS++;
10                    i--;
11                }else if(skipS >0){
12                    skipS--;
13                    i--;
14                }else{
15                    break;
16                }
17            }
18            while(j>=0){
19                if(t.charAt(j) == '#'){
20                    skipT++;
21                    j--;
22                }else if(skipT >0){
23                    skipT--;
24                    j--;
25                }
26                else{
27                    break;
28                }
29            }
30            if(i>=0 && j>=0 && s.charAt(i) != t.charAt(j)){
31                return false;
32            }
33            if((i>=0) != (j>=0)){
34                return false;
35            }
36            i--;
37            j--;
38        }
39        return true;
40    }
41}