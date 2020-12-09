class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        // use hashmap to score remainder of 60 of each song's time
        // then we just need to loop for each song and check whether
        // its complement remainder of 60 is in the map
        Map<Integer, Integer> count = new HashMap<>();
        
        int res = 0;
        for (int t : time) {
            int r = t%60;
            int comp = (r == 0) ? 0 : 60 - r;
            res += count.getOrDefault(comp, 0);
            count.put(r, count.getOrDefault(r, 0) + 1);
        }
        return res;
    }
}