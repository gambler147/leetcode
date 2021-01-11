# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # there are different cases, assume n is the length of the linkedlist
        # let k = min(k, n-k+1)
        # 1. n == 0, simply return None
        # 2. n == 1, do nothing, return head
        # 3. n == 2, swap head and head.next (tail)
        # 4. n > 2, k == 1, swap head and tail
        # 5. n > 2, k == n - k + 1, do nothing
        # 6. n > 2, n-2*k+1==1, swap these two neighbor elements
        # 7. n > 2, n-2*k+1>1
        
        # first find length of the linkedlist
        n = 0
        node = head
        while node:
            n+=1
            node = node.next
            
        k = min(k, n-k+1)
        # case 1
        if n == 0: return None
        
        # case 2
        if n == 1: return head
        
        # case 3
        if n == 2:
            tail = head.next
            tail.next = head
            head.next = None
            return tail
        
        # case 4
        if n > 2 and k == 1:
            # find second last node
            node = head
            while node.next.next != None:
                node = node.next
            tail = node.next
            tail.next = head.next
            node.next = head
            head.next = None
            return tail
        
        # case 5
        if n > 2 and k == n-k+1:
            return head
        
        # case 6
        if n > 2 and n-2*k+1 == 1:
            # find k-1th node
            node = head
            while k > 2:
                node = node.next
                k-=1
                
            l = node.next
            r = l.next
            l.next = r.next
            r.next = l
            node.next = r
            return head
        
        # case 7
        if n > 2 and n-2*k+1 > 1:
            # find k-1th node and n-k th node
            t = k-2
            n1, n2 = head, head
            while t > 0:
                n1 = n1.next
                t -= 1
                
            t = n-k-1
            while t > 0:
                n2 = n2.next
                t -= 1
                
            l = n1.next
            r = n2.next
            p1 = l.next
            p2 = r.next
            n1.next = r
            n2.next = l
            l.next = p2
            r.next = p1
            return head
        
        return None
        
            