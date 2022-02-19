class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        map2 = {v: idx for idx, v in enumerate(nums2)}
        # convert nums2 to match the ordering of nums1
        for i, v in enumerate(nums1):
            nums2[map2[v]] = i+1
            
        # now we only care about nums2's number of increasing triplets
        # I use a binary indexed tree for O(logn) searching and updating        
        def update(BIT, n, i, val):
            while i <= n:
                BIT[i] += val
                i += (i & -i)
                
        def query(BIT, i):
            s = 0
            while i > 0:
                s += BIT[i]
                i -= (i & -i)
            return s
        
        # build a BIT
        BIT = [0] * (n + 1)
        left_small = [0] * (n+1)
        right_great = [0] * (n+1)
        
        for i in range(n-1, -1, -1):
            right_great[i] = (n-i-1) - query(BIT, nums2[i] - 1)
            update(BIT, n, nums2[i], 1)
        
        # clear BIT
        for i in range(n+1):
            BIT[i] = 0
                
        for i in range(n):
            left_small[i] = query(BIT, nums2[i])
            update(BIT, n, nums2[i], 1)
            
        res = 0
        for i in range(n):
            res += left_small[i] * right_great[i]
            
        return res
        
