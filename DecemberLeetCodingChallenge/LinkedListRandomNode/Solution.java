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
import java.util.concurrent.ThreadLocalRandom;
class Solution {
    int size=0;
    ListNode head;
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        this.head = head;
    }
    
    /** Returns a random node's value. */
    public int getRandom() {
        /* reservoir sampling
        we iterate the whole linked list, start with counter i = 1 and set result node as the head
        for each iteration, with counter i, we replace our res with new node with probability of 1/i
        in this case, for each node (ith position), the probabilty that this node be the final 
        remaining node is 1/i (replace old res with prob 1/i) * i/(i+1) * ... * (n-1)/n = 1/n
        */
        int i=0;
        ListNode node = this.head;
        ListNode res = this.head;
        while (node != null) {
            i++;
            int j = ThreadLocalRandom.current().nextInt(i);
            if (j == 0) {
                res = node;
            }
            node = node.next;
        }

        return res.val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */