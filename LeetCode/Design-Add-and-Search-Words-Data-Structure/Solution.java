1class WordDictionary {
2
3    private static class TrieNode{
4        TrieNode[] children = new TrieNode[26];
5        boolean isEnd = false;
6    }
7    private final TrieNode root; 
8
9    public WordDictionary() {
10        root = new TrieNode();
11    }
12    
13    public void addWord(String word) {
14        TrieNode curr = root;
15        for(char c: word.toCharArray()){
16            int idx = c-'a';
17            if(curr.children[idx] == null){
18                curr.children[idx] = new TrieNode();
19            }
20            curr = curr.children[idx];
21        }
22        curr.isEnd = true;
23    }
24    
25    public boolean search(String word) {
26        return searchHelper(word, 0, root);
27    }
28    private boolean searchHelper(String word, int index, TrieNode node){
29        if(node == null) return false;
30        if(index==word.length()){
31            return node.isEnd;
32        }
33        char c = word.charAt(index);
34        if(c == '.'){
35            for(int i =0; i<26; i++){
36                if(node.children[i] !=null){
37                    if(searchHelper(word, index+1, node.children[i])){
38                        return true;
39                    }
40                }
41            }
42            return false;
43        }else{
44            int idx = c-'a';
45            return searchHelper(word, index+1, node.children[idx]);
46        }
47    }
48}
49
50/**
51 * Your WordDictionary object will be instantiated and called as such:
52 * WordDictionary obj = new WordDictionary();
53 * obj.addWord(word);
54 * boolean param_2 = obj.search(word);
55 */