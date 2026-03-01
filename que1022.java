
//Not to use class TreeNode in LeetCode, but to use it in local testing
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
    public int sumRootToLeaf(TreeNode root) {
        return dfs(root,0);
    }
    private int dfs (TreeNode node, int current){
        if(node == null) return 0;
        current = (current << 1) | node.val;

        if(node.left == null && node.right == null){
            return current;
        } 
        return dfs(node.left, current) + dfs(node.right,  current);
    }
}