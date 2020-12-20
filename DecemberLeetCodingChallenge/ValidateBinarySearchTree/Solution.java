/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MAX_VALUE, Long.MIN_VALUE);
        
    }
    
    public boolean dfs(TreeNode node, long upper, long lower) {
        // check if subtree is a bst with given upper bound and lower bound
        if (node == null) return true;
        
        if (node.val >= upper || node.val <= lower) return false;
        
        boolean ans = true;
        
        ans &= dfs(node.left, Math.min(node.val, upper), lower);
        ans &= dfs(node.right, upper, Math.max(node.val, lower));
        
        return ans;
        
        
    }
}