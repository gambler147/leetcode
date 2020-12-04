class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        /* monotonous decreasing queue O(n)*/
        int n = nums.length;
        Deque<Integer> deque = new ArrayDeque<>();
        
        // intialization with k values
        for (int i=0; i<k; i++) {
            while (deque.size() > 0 && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast();
            }
            deque.addLast(i);
        }
        
        int[] res = new int[n-k+1];
        res[0] = nums[deque.peekFirst()];
        for (int i=k; i<n; i++) {
            while (deque.size() > 0 && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast();
            }
            deque.addLast(i);
            // pop elements that is before current window
            while (deque.peekFirst() <= i-k) {
                deque.pollFirst();
            }
            res[i-k+1] = nums[deque.peekFirst()];
        }
        return res;
    }
}