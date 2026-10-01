1class Solution {
2    public String decodeString(String s) {
3        Stack<Integer> numStack = new Stack<>();
4        Stack<StringBuilder> strStack = new Stack<>();
5        StringBuilder currentStr = new StringBuilder();
6        int currentNum = 0;
7        for(char c: s.toCharArray()){
8            if(Character.isDigit(c)){
9                currentNum = currentNum*10+(c-'0');
10            }else if (c=='['){
11                numStack.push(currentNum);
12                strStack.push(currentStr);
13                currentStr = new StringBuilder();
14                currentNum = 0;
15            }else if(c==']'){
16                int repeatTimes = numStack.pop();
17                StringBuilder prevStr = strStack.pop();
18                for(int i=0; i<repeatTimes; i++){
19                    prevStr.append(currentStr);
20                } 
21                currentStr = prevStr;
22            }else{
23                currentStr.append(c);
24            }
25        }
26        return currentStr.toString();
27    }
28}