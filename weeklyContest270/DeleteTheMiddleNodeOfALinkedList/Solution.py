# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        node = head
        while node is not None:
            node = node.next
            n += 1
        
        if n == 1:
            return None
        
        k = n//2
        node = head
        prev = None
        while k > 0:
            prev = node
            node = node.next
            k -= 1
        
        # middle node found
        prev.next = node.next
        return head
