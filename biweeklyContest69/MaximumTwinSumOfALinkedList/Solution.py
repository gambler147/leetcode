# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        
        res = 0
        n = len(vals)
        for i in range(n//2):
            res = max(res, vals[i] + vals[n-i-1])
        return res
    
