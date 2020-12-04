class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        Stack<int[]> stack = new Stack<>();
        // iterate intervals
        for (int i=0; i<intervals.length; i++) {
            int[] p = intervals[i];
            while ((stack.size() > 0) && (p[0] <= stack.peek()[1])) {
                int[] last = stack.pop();
                p[0] = Math.min(p[0], last[0]);
            }
            stack.push(p);
        }
        // convert to array
        int[][] res = new int[stack.size()][2];
        int i=0;
        for (int[] p : stack) {
            res[i++] = p;
        }
        
        return res;
    }
}