class Solution {
    public int longestMountain(int[] arr) {
        if (arr.length < 3) return 0;
        // use cur to record number of elements up to current point, which can be potential mountain
        int cur = 1;
        int res = 0;
        boolean up = true; // is uphill
        for (int i=1; i<arr.length; i++) {
            if (arr[i] > arr[i-1]) {
                if (up == true) {
                    cur++;
                } else {
                    res = Math.max(cur, res);
                    cur = 2;
                    up = true;
                }
            } else if (arr[i] < arr[i-1]) {
                if (cur >= 2) {
                    up = false;
                }  
                
                if (up == false) {
                    cur++;
                    res = Math.max(cur, res);
                } else {
                    cur = 1;
                }
            } else {
                cur = 1;
            }
        }
        
        return res;
    }
}