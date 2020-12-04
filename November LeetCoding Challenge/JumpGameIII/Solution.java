class Solution {
    public boolean canReach(int[] arr, int start) {
        int n = arr.length;
        // status[i] == 0 means not vistied yet, 1 means possible, -1 means
        // impossible
        Set<Integer> visited = new HashSet<>();
        Stack<Integer> stack = new Stack<>(); // similar to dfs
        stack.push(start);
        
        while (stack.size() > 0) {
            int pos = stack.pop();
            visited.add(pos);
            if (arr[pos] == 0) {
                return true;
            }
            if (pos + arr[pos] < n && !visited.contains(pos + arr[pos])) {
                stack.push(pos + arr[pos]);
            }
            if (pos - arr[pos] >= 0 && !visited.contains(pos - arr[pos])) {
                stack.push(pos - arr[pos]);
            }
        }
        return false;
    }
}