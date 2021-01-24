class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] res = new int[n];
        int sum = 0;
        int l=1, r=k;
        if (k < 0) {
            k = -k;
            l = n-k;
            r = n-1;
        }
        
        for (int i=l; i<=r; i++) {
            sum += code[i];
        }
        
        for (int i=0; i<n; i++) {
            res[i] = sum;
            sum -= code[(l++)%n];
            sum += code[(++r)%n];
        }
        return res;
    }
}
