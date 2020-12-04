class Solution {
    public boolean canPartition(int[] nums) {
        /* 
        record number of occurences of each possible sum from 0 to sum(nums), 
        we just need to check if (sum == total_sum/2) exist
        */
        int n=nums.length;
        int sum = 0;
        for (int i=0; i<n; i++) {
            sum += nums[i];
        }
        if (sum%2 == 1) return false;
        
        Map<Integer, Integer> sum_map = new HashMap<>();
        sum_map.put(0, 1);
        for (int num: nums) {
            Map<Integer, Integer> tmp = new HashMap<>();
            for (int presum : sum_map.keySet()) {
                tmp.put(presum+num, sum_map.get(presum));
            }
            tmp.forEach((k, v) -> sum_map.merge(k,v, (v1,v2) -> v1+v2));
        }
        
        return sum_map.containsKey(sum/2) ? true : false;
    }
}