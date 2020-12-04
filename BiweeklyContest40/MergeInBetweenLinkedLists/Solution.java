/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode A;
        ListNode B;
        
        A = list1;
        b -= a;
        // find parent of first node
        while (a-- > 1) {
            A = A.next;
        }
        // find child of second node
        B = A;
        while (b-- >= -1) {
            B = B.next;
        }
        // concatenate
        A.next = list2;
        ListNode C = list2;
        while (C != null && C.next != null) {
            C = C.next;
        }
        C.next = B;
        return list1;
        
    }
}