class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        // count consecutive 0s
        // for initial position, we add one 0 to the front, which makes it easier for calculation
        int cur = 1;
        int res = 0;
        for (int v : flowerbed) {
            if (v == 0) {
                cur++;
            } else {
                res += (cur-1) / 2;
                cur = 0;
            }
        }
        res += cur / 2;
        return res >= n;
    }
}