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
    public TreeNode increasingBST(TreeNode root) {
        TreeNode prev=null;
        TreeNode cur=root;
        TreeNode newRoot = null;
        
        while (cur != null) {
            if (cur.left != null) {
                TreeNode lrm = rightMost(cur.left);
                TreeNode tmp = cur.left;
                lrm.right = cur;
                if (prev != null) {
                    prev.right = cur.left;
                } 
                cur.left = null;
                cur = tmp;
            } else {
                if (newRoot == null) {
                    newRoot = cur;
                }
                prev=cur;
                cur = cur.right;
            }
        }
        return newRoot;
    }
    public TreeNode rightMost(TreeNode root) {
        /* return rightmost(largest) node in the tree given root */
        while (root.right != null) {
            root = root.right;
        }
        return root;
    }
}