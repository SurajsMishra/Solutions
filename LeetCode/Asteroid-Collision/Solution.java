1class Solution {
2    public int[] asteroidCollision(int[] asteroids) {
3        Stack<Integer> stack = new Stack<>();
4        for(int ast: asteroids){
5            boolean exploded = false;
6            while (!stack.isEmpty() && stack.peek() > 0 && ast<0){
7                if(stack.peek() < -ast){
8                    stack.pop();
9                    continue;
10                }else if(stack.peek() == -ast){
11                    stack.pop();
12                    exploded = true;
13                    break;
14                }else{
15                    exploded = true;
16                    break;
17                }
18            }
19            if(!exploded){
20                stack.push(ast);
21            }
22        }
23        int[] result = new int[stack.size()];
24        for (int i = result.length - 1; i>=0; i--){
25            result[i] = stack.pop();
26        }
27        return result;
28    }
29}