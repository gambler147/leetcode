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
    int res = 0;
    public int pseudoPalindromicPaths (TreeNode root) {
        Set<Integer> set = new HashSet<>();
        dfs(root, set);
        return this.res;
    }
    
    public void dfs(TreeNode node, Set<Integer> set) {
        // if visiting the leaf node, check size of set
        // is size == 0 or 1, res++
        // else ignore
        if (node == null) return;
        if (set.contains(node.val)) {
            set.remove(node.val) ;
        } else {
            set.add(node.val);
        }
        
        if (node.left == null && node.right == null) {
            if (set.size() <= 1) {
                this.res++;
            }
        }
        else {
            dfs(node.left, set);
            dfs(node.right, set);
        }
        if (set.contains(node.val)) {
            set.remove(node.val) ;
        } else {
            set.add(node.val);
        }
    }
}
