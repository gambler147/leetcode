class Solution {
    public int smallestRangeII(int[] A, int K) {
        // consider A is sorted, ideally we subtract large numbers by K and 
        // add small numbers by K, if there is an optimal solution, we must
        // have an index i, such that for j <= i, A[j] -> A[j] + K and 
        // for j > i, A[j] -> A[j] - K. Then the max difference is 
        // max(A[i]-A[i+1]+2K, A[n-1] - A[0] - 2K, A[i]-A[0], A[n-1]-A[i+1])
        // we find minimum value for all i
        // also notice a trivial case is let x = K (-K) for all i
        Arrays.sort(A);
        
        int n = A.length;
        int res = A[n-1] - A[0];
        for (int i=0; i<n-1; i++) {
            Integer[] candidates = {A[i]-A[i+1]+2*K, A[n-1]-A[0]-2*K, A[i]-A[0], A[n-1]-A[i+1]};
            res = Math.min(res, Collections.max(Arrays.asList(candidates)));
        }
        return res;
    }
}