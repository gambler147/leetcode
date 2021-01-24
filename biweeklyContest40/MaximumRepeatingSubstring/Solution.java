class Solution {
    public int maxRepeating(String sequence, String word) {
        int n = sequence.length();
        int m = word.length();
        
        if (m > n) return 0;
        int[] dp = new int[n];
        
        int res = 0;
        for (int i=0; i<=n-m; i++) {
            for (int j=0; j<m; j++) {
                if (word.charAt(j) != sequence.charAt(i+j)) {
                    break;
                }
                if (j == m-1) dp[i] = (i-m >= 0) ? dp[i-m] + 1 : 1;
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}