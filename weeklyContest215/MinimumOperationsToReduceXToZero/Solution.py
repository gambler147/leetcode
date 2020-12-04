class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # longest subarray with sum equal to sum(nums) - x
        s = sum(nums) - x
        if s == 0: return len(nums)

        seen = collections.defaultdict(int)
        seen[0] = -1
        prefix = 0
        res = -1
        for i in range(len(nums)):
            seen 
            prefix += nums[i]
            if prefix - s in seen:
                res = max(i - seen[prefix-s], res)
                
            seen.setdefault(prefix, i)
        
        return len(nums) - res if res != -1 else -1
        
