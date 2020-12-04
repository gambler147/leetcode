class Solution {
    public boolean canDistribute(int[] nums, int[] quantity) {
        // backtracking
        // first calculate count of each number we get an array with each element being the count of a unique number
        // then for each quantity, we iterate each element in count, if quantity[i] <= count[j], we proceed otherwise
        // we try count[j+1]
        
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        
        // turn counter to array, we do not need the key
        int[] carr = new int[counter.size()];
        int i = 0;
        for (int key : counter.keySet()) {
            carr[i++] = counter.get(key);
        }
        
        // sort quantity and carr
        Arrays.sort(carr);
        Arrays.sort(quantity);
        reverse(quantity);
        return solve(carr, quantity, 0);
    }
    
    public void reverse(int[] arr) {
        // reverse array
        int n = arr.length;
        for (int i=0; 2*i < n; i++) {
            int tmp = arr[i];
            arr[i] = arr[n-i-1];
            arr[n-i-1] = tmp;
        }
    }
    
    public boolean solve(int[] carr, int[] quantity, int idx) {
        // return true if we can allocate quantity from i to the end using carr
        int m = quantity.length;
        int n = carr.length;
        if (idx >= m) return true; // we already went through all quantities
        
        for (int i=0; i<n; i++) {
            if (carr[i] >= quantity[idx]) {
                // we can satisfy quantity[idx]
                carr[i] -= quantity[idx];
                if (solve(carr, quantity, idx+1)) {
                    return true;
                }
                carr[i] += quantity[idx];
            }
        }
        return false;
    }
}

/*
Solution 2: bit mask and dfs

class Solution {
    int m;
    int n;
    Map<Pair<Integer, Integer>, Boolean> dp = new HashMap<>();
    int[] carr;
    int[] mask_sum; // mask_sum[mask] maintains sum of the subset sum of quantity
    public boolean canDistribute(int[] nums, int[] quantity) {
        // dp and bitmask O(50 * 3^m)
        // we calculate counter of each number in nums and get the array
        // for each mask, the 1s in its binary representation are subset in quantity indices that we are going to check
        // if it satistfy counter[i] >= sum, e.g. if mask is 00101, and i is 0, we check whether we can satisfy
        // quantity[2] + quantity[0] >= counter[0], if so we check the bitwise mask of 11010 and move i to i+1 and so forth
        
        Map<Integer, Integer> counter = new HashMap<>();
        // dp[(i, mask)] returns true if mask can be satisfied by car[ri]
        // initialize counter
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        // we just need the value of counter
        carr = new int[counter.size()];
        int k=0;
        for (int key : counter.keySet()) {
            carr[k++] = counter.get(key);
        }
        
        m = quantity.length;
        n = carr.length;
        
        // initialize mask_sum
        mask_sum = new int[1<<m];
        for (int mask=0; mask < (1<<m); mask++) {
            for (int i=0; i<m; i++) {
                if ((1<<i & mask) != 0) {
                    mask_sum[mask] += quantity[i];
                }
            }
        }
        // dp
        int mask = (1 << m) - 1;  // full set
        return dfs(0, mask);
        
    }
    
    public boolean dfs(int i, int mask) {
        if (mask == 0) return true;
        if (i >= n) return false;
        
        Pair pair = new Pair(i, mask);
        if (dp.containsKey(pair)) {
            return dp.get(pair);
        }
        
        // using submask to check if subsets of mask can be satisfied by carr[i]
        int submask = mask;
        while (submask != 0) {
            if (mask_sum[submask] <= carr[i] && dfs(i+1, submask ^ mask)) {
                dp.put(pair, true);
                return true;
            }
            submask = (submask - 1) & mask; // next subset mask from mask
        }
        // we cannot satisfy any subset using carr[i], we jump to carr[i+1] for the whole mask
        dp.put(pair, dfs(i+1, mask));
        return dp.get(pair);
    }
}

*/
