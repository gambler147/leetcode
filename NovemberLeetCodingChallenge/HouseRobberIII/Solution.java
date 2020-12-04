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
    public int rob(TreeNode root) {
        int[] res = dfs(root);
        return Math.max(res[0], res[1]);
    }
    
    public int[] dfs(TreeNode node) {
        // find out maximum profit starting from node
        // return [maximum profit including node, maximum profit without node]
        
        if (node == null) {
            return new int[] {0, 0};
        }
        
        int[] left = dfs(node.left);
        int[] right = dfs(node.right);
        
        // maximum profit containing current node is left[1] + right[1] + node.val
        // maximum profit without current node is max(left[0], left[1]) + max(right[0], right[1])
        int wt = left[1] + right[1] + node.val;
        int wo = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        
        return new int[] {wt, wo};
    }
}