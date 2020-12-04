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
    int res=0;
    public int rangeSumBST(TreeNode root, int low, int high) {
        dfs(root, low, high);
        return this.res;
    }
    
    public void dfs(TreeNode node, int low, int high) {
        if (node == null) return;
        if (node.val >= low && node.val <= high) {
            this.res += node.val;
        }
        
        if (node.val > low) {
            dfs(node.left, low, high);
        }
        
        if (node.val < high) {
            dfs(node.right, low, high);
        }
        return;
    }
}
