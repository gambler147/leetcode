class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # map value to indices
        # Time complexity O(n + q * 100) where n is size of nums and q is size of queries
        val_to_ind = collections.defaultdict(list)
        for i, v in enumerate(nums):
            val_to_ind[v].append(i)
            
        res = []
        for q, (l,r) in enumerate(queries):
            # find all posible values that are present in interval [l,r]
            vals = []
            for v in val_to_ind.keys():
                li = bisect.bisect_left(val_to_ind[v], l)
                if li < len(val_to_ind[v]) and val_to_ind[v][li] <= r:
                    vals.append(v)
                    
            vals.sort()
            res.append(min([vals[i+1] - vals[i] for i in range(len(vals)-1)] or [-1]))
        return res
        