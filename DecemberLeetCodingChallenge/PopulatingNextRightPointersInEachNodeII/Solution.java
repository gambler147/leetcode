/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        dfs(root);
        return root;
    }
    
    public void dfs(Node root) {
        // point node's left child to node's right child if exist else
        // we iterate through nodes' next node
        if (root == null) return;

        Node prev = null;
        Node node = root;
        while (node != null) {
            if (node.left != null) {
                if (prev != null) {
                    prev.next = node.left;
                }
                prev = node.left;
            }
            
            if (node.right != null) {
                if (prev != null) {
                    prev.next = node.right;
                }
                prev = node.right;
            }
            node = node.next;
        }
        dfs(root.left);
        dfs(root.right);
    }
}