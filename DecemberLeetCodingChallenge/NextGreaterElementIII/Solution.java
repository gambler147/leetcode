class Solution {
    public int nextGreaterElement(int n) {
        // use a list
        List<Integer> digits = new ArrayList<>();
        // reversed digits, list
        while (n>0) {
            int r = n%10;
            int q = n/10;
            digits.add(r);
            n = q;
        }
        // find first index i such that digits[i] > digits[i+1]
        int idx = -1;
        for (int i = 0; i < digits.size() - 1; i++) {
            if (digits.get(i) > digits.get(i+1)) {
                idx = i+1;
                break;
            }
        }
        // if not found, then return -1
        if (idx == -1) return -1;
        // otherwise, find firxt index j < idx such that digits[j] > digits[idx]
        // and swap digits[idx] and digits[j]
        int jdx = 0;
        for (int j =0; j<idx; j++) {
            if (digits.get(j) > digits.get(idx)) {
                jdx = j;
                break;
            } 
        }
        // swap idx and jdx
        int tmp = digits.get(jdx);
        digits.set(jdx, digits.get(idx));
        digits.set(idx, tmp);
        // reverse digits[0:idx]
        int l=0, r=idx-1;
        while (l < r) {
            tmp = digits.get(l);
            digits.set(l, digits.get(r));
            digits.set(r, tmp);
            l++;
            r--;
        }
        // now reconstruct the number
        long res = 0;
        int d;
        for (int i=digits.size()-1; i>=0; i--) {
            d = digits.get(i);
            res = res*10 + d;
        }
        return res > Integer.MAX_VALUE ? -1 : (int) res;
    }
}

