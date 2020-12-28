class Solution {
    public int reachNumber(int target) {
        // suppose target is a positive number
        // find n such that n(n+1)/2 >= T
        // if n(n+1)/2 == T return n
        // else if n(n+1)/2 > T and r := n(n+1)/2 - T is an odd number
        //          if n+1 is odd, return n+1
        //          if n+1 is even return n+2
        // else if n(n+1)/2 > t and n(n+1)/2 - T is an even number, return n
        
        if (target < 0) target = -target;
        
        // binary search to find n such that n(n+1) >= 2T
        int i = 0, j = target;
        while (i < j) {
            int m = (i+j) >> 1;
            if ((long) m*(m+1)/2 >= target) {
                j = m;
            } else {
                i = m+1;
            }
        }
        int r = i*(i+1)/2 - target;
        if (r%2==0) {
            return i;
        } else {
            return i+1 + (i%2 == 0 ? 0 : 1);
        }
    }
}

