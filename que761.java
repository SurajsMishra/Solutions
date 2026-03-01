import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
class Solution {
    public String makeLargestSpecial(String s) {
        List<String> list =new ArrayList<>();
        int balance = 0;
        int start = 0;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == '1') balance++;
            else balance--;
            if(balance == 0){
                String inner = s.substring(start+1 ,i);
                String result ='1' +makeLargestSpecial(inner) + "0";
                list.add(result);
                start = i+1;
            }
        }
        Collections.sort(list,Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for(String str: list){
            sb.append(str);
        }
        return sb.toString();
    }
}