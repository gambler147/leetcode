# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        # 1. notice that for each value, there can be only two occurences and one must be root and the other must be leaf
        # 2. in the final tree, there cannot be duplicate values
        # 3. root whose value is not present in any of the leaf values must be the root of final tree
        # 4. tree with single root can not be the root of final tree
        # We first look through all roots to determine which root is the final root (if there are multiple candidates, 
        # then it is impossible to merge). Starting from the candidate, we get the leaves, then check if any leaf can
        # be merged with any of the remaining root, if so, we force a merge and update the leaves. Do this process until
        # no roots left or no leaf values matched with roots.
        # So far, if there are roots not merged, return null. Otherwise and at last, we check if there merged tree is 
        # a valid binary search tree, if so we return the final root other wise return null.
        
        n = len(trees)
        root_val_to_root = {} # map root value to root node
        leaf_values = set() # map leaf value to leaf node
        
        # construct mappings
        def get_leaf_nodes(root):
            leafs = []
            def _get_leaf_nodes(node, is_root=True):
                if node is not None:
                    if not node.left and not node.right and not is_root:
                        leafs.append(node)
                    _get_leaf_nodes(node.left, is_root=False)
                    _get_leaf_nodes(node.right, is_root=False)
            _get_leaf_nodes(root,is_root=True)
            return leafs
                
                
        def merge(leaf, root):
            # merge leaf node and root
            if root.left:
                leaf.left = TreeNode(root.left.val)
                merge(leaf.left, root.left)
            if root.right:
                leaf.right = TreeNode(root.right.val)
                merge(leaf.right, root.right)
            
        for root in trees:
            root_val_to_root[root.val] = root
            leaves = get_leaf_nodes(root)
            leaf_values.update((leaf.val for leaf in leaves))
        # deterine the root of final tree
        candidates = [k for (k,v) in root_val_to_root.items() if k not in leaf_values]
        if len(candidates) != 1:
            return None
        
        ftree_root = root_val_to_root.pop(candidates[0])
        # loop through the tree and merge other roots to current tree
        # get leaves of current tree
        fleaves = get_leaf_nodes(ftree_root)
        cnt = 1 # merged tree
        while fleaves and len(root_val_to_root):
            leaf = fleaves.pop()
            root = root_val_to_root.get(leaf.val, None)
            if root:
                # merge if exisits
                merge(leaf, root)
                root_val_to_root.pop(leaf.val)
                # update fleaves
                for l in get_leaf_nodes(leaf):
                    fleaves.append(l)
                cnt += 1
                
        print(cnt)
        # if cnt is not n, return False
        if cnt != n:
            return None
        
        # then verify the final tree is a valid BST
        def is_valid_bst(root):
            # in order traversal
            stack = []
            prev = None # previous node value
            node = root
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                
                node = stack.pop()
                if prev is not None and node.val <= prev:
                    return False
                # update prev
                prev = node.val
                node = node.right
            return True
        
        return ftree_root if is_valid_bst(ftree_root) else None
            
                