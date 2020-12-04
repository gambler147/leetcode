class Solution {
    public int minimumMountainRemovals(int[] nums) {
        // same as longest increasing/decreasing subsequences
        int n = nums.length;
        
        int[] inc = new int[n]; // length of left side longest increasing array up to i
        int[] dec = new int[n]; // length of right side longest increasing array from n-1 to i
        for (int i=1; i<n; i++) {
            for (int j=0; j<i; j++) {
                if (nums[j] < nums[i]) {
                    inc[i] = Math.max(inc[i], inc[j] + 1);
                }
            }
        }
        
        for (int i=n-2; i>=0; i--) {
            for (int j=n-1; j>i; j--) {
                if (nums[j] < nums[i]) {
                    dec[i] = Math.max(dec[i], dec[j] + 1);
                }
            }
        }
        
        // find maximum value of inc[i] + dec[i] + 1
        int res=0;
        for (int i=0; i<n; i++) {
            if (inc[i] == 0 || dec[i] == 0) continue;
            res = Math.max(inc[i] + dec[i] + 1, res);
        }
        return n-res;
    }
}