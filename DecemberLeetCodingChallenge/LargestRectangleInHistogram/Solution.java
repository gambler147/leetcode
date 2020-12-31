class Solution {
    public int largestRectangleArea(int[] heights) {
        // non-decreasing stack
        int n = heights.length;
        if (n == 0) return 0;
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        for (int i=0; i<n; i++) {
            // while current height is smaller than last height in the stack
            // pop out the stack and calculate the area from popped out index (j) to i
            while (stack.size() > 0 && heights[stack.peek()] > heights[i]) {
                int j = stack.pop();
                int last = stack.size() > 0 ? stack.peek() : -1;
                int area = (i - last - 1) * heights[j];
                res = Math.max(res, area);
            }
            stack.push(i);
        }
        // deal with the final monotonic increasing stack
        
        while (stack.size() > 0) {
            int j = stack.pop();
            int last = stack.size() > 0 ? stack.peek() : -1;
            int area = (n-last-1)*heights[j];
            res = Math.max(res, area);
        }
        return res;
    }
}
