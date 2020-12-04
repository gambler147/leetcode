class Solution {
    int a;
    int b;
    int x;
    int max;
    Set<Integer> forbidden = new HashSet<>();
    Set<Pair<Integer, Boolean>> seen = new HashSet<>();
    
    int res = Integer.MAX_VALUE;
    public int minimumJumps(int[] forbidden, int a, int b, int x) {
        // dfs
        this.a = a;
        this.b = b;
        this.x = x;
        this.max = x;
        for (int i=0; i<forbidden.length; i++) {
            max = Math.max(max, forbidden[i]);
        }
        max += a + b;

        for (int f : forbidden) {
            this.forbidden.add(f);
        }
        
        dfs(0, 0, false);
        return res == Integer.MAX_VALUE ? -1 : res;
        
    }
    
    public void dfs(int i, int jumps, boolean backwards) {
        if (this.forbidden.contains(i)) return;
        Pair loc = new Pair(i, backwards);
        
        if (seen.contains(loc)) return;
        seen.add(loc);
        if (i == x) {
            res = Math.min(res, jumps);
        }
        if (i < 0 || i > max) return;
        
        dfs(i+a, jumps+1, false);
        if (!backwards) {
            dfs(i-b, jumps+1, true);
        }
        return;
        
    }
}

