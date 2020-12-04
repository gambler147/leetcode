class Solution {
    public int minimumDeletions(String s) {
        // iterate for each position i, find number of 'b's before i and number of 'a's after i, 
        // the total number of deletion is the sum
        int n =s.length();
        int a=0;
        int b=0;
        int res = Integer.MAX_VALUE;
        for (int i=0; i<n; i++) {
            if (s.charAt(i) == 'a') {
                a++;
            }
        }
        
        for (int i=0; i<n; i++) {
            if (s.charAt(i) == 'a') {
                a--;
            } else {
                res = Math.min(res, a+b);
                b++;
            }
        }
        // in case the last char is 'a'
        res = Math.min(res, b);
        return res;
    }
}
