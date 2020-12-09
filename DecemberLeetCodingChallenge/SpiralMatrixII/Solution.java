class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        // initially moving horizontally
        int rm = 0;
        int cm = 1; 
        int i=0, j=0; // initial position
        for (int val=1; val <= n*n; val++) {
            res[i][j] = val;
            if (!((i+rm<n) && (i+rm>=0) && (j+cm<n) && (j+cm>=0) && res[i+rm][j+cm] == 0)) {
                // change direction
                int tmp = rm;
                rm = cm;
                cm = -tmp;
            }
            i+=rm;
            j+=cm;
        }
        return res;
    }
}