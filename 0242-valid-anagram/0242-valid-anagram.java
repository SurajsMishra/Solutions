class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        Map<Character, Integer> map = new HashMap<>();
        for(int i =0; i<s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                int freq = map.get(s.charAt(i));
                map.put(s.charAt(i), ++freq);
            }else{
                map.put(s.charAt(i), 1);
            }
        }
        for(int j =0; j<t.length(); j++){
            if(map.containsKey(t.charAt(j))){
                int freq = map.get(t.charAt(j));
                map.put(t.charAt(j), --freq);
            }else{
                map.put(t.charAt(j), 1);
            }
        }
        for(int i =0; i<s.length(); i++){
            if(map.get(s.charAt(i)) != 0){
                return false;
            }
        }
        return true;
    }
}