class Solution {
    public int mirrorReflection(int p, int q) {
        // find lcm of (p,q) as k, then the laser have k/p - 1 reflections on the top|bottom mirror
        // and k/q - 1 reflections on the left|right mirror. just need to find the parity of 
        // k/p-1 and k/q - 1
        int k = lcm(p, q);
        int hrefl = k/p-1;  // top|bottom reflections
        int vrefl = k/q-1;  // left | right reflections
        
        if ((hrefl & 1) == 1) {
            return 0;
        } else if ((vrefl&1) == 1) {
            return 2;
        } else {
            return 1;
        }
        
    }
    
    public int gcd(int p, int q) {
        if (q > p) {
            int t = p;
            p = q;
            q = p;
        }
        
        int temp;
        int r = q; // remainder
        while (r > 0) {
            temp = p%r;
            p = r;
            r = temp;
        }
        return p;
    }
    
    public int lcm(int p, int q) {
        int m = gcd(p, q);
        return (p*q) / m;
    }
}