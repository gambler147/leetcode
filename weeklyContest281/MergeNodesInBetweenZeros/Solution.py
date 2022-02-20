# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        new_head = ListNode(0)
        prev = new_head
        cur_val = 0
        while node:
            if node.val == 0 and cur_val > 0:
                # creat a new list node
                new_node = ListNode(cur_val)
                prev.next = new_node
                prev = new_node
                cur_val = 0
            elif node.val != 0:
                cur_val += node.val
            
            node = node.next
            
        if cur_val > 0:
            new_node = ListNode(cur_val)
            prev.next = new_node
            
        return new_head.next
                
