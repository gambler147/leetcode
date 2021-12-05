# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # dfs
        self.dfs(root, startValue, destValue, [], [])
        # find first string both string diverges
        m, n = len(self.startStr), len(self.destStr)
        k = 0
        for i in range(min(m,n)):
            if i+1 >= min(m,n) or self.startStr[i+1] != self.destStr[i+1]:
                k = i
                break
        # reconstruct the path
        path = 'U'*(m-k-1) + ''.join(self.destPath[k:])
        return path
        
        
    def dfs(self, node, s, d, digit_list, path_list):
        # if current value is start value or dest value, stop and return the flag
        if node is None:
            return
        
        digit_list.append(node.val)
        if node.val == s:
            # copy path
            self.startStr = copy.deepcopy(digit_list)
            self.startPath = copy.deepcopy(path_list)
        
        if node.val == d:
            self.destStr = copy.deepcopy(digit_list)
            self.destPath = copy.deepcopy(path_list)
        
        # go to the left
        path_list.append('L')
        self.dfs(node.left, s, d, digit_list, path_list)
        path_list.pop()
        
        # go to the right
        path_list.append('R')
        self.dfs(node.right, s, d, digit_list, path_list)
        path_list.pop()
        
        # pop current node
        digit_list.pop()
        
        