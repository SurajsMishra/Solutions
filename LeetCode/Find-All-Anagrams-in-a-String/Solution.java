1class Solution {
2    public List<Integer> findAnagrams(String s, String p) {
3        List<Integer> result= new ArrayList<>();
4        int sLen = s.length();
5        int pLen = p.length();
6        if(sLen<pLen){
7            return result;
8        }
9        int[] pCount = new int[26];
10        int[] sCount = new int[26];
11        for (int i =0; i<pLen; i++){
12            pCount[p.charAt(i) - 'a']++;
13            sCount[s.charAt(i) - 'a']++;
14        }
15        if(Arrays.equals(pCount, sCount)){
16            result.add(0);
17        }
18        for(int i=pLen; i<sLen; i++){
19            sCount[s.charAt(i) - 'a']++;
20            sCount[s.charAt(i-pLen) - 'a']--;
21            if(Arrays.equals(pCount, sCount)){
22                result.add(i-pLen+1);
23            }
24        }
25        return result;
26    }
27}