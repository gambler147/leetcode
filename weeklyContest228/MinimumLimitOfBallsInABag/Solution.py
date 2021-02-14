class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # binary search, O(log(max(nums))), 
        # to check if given cost is achievable, go through the list
        # and find number of operations needed to divide balls into
        # 2 new bags with balls fewer than target. And the operations
        # required is ceil(num / target)
        
        def helper(nums, target, maxOperations):
            # return true if given target is achievable else false
            cnt = 0
            for d in nums:
                if d > target:
                    cnt += d//target if d%target else d//target-1
                if cnt > maxOperations:
                    return False
            return True
        
        # binary search
        l, r = 1, max(nums)
        while l < r:
            m = (l+r) >> 1
            if helper(nums, m, maxOperations):
                r = m
            else:
                l = m+1
        return l
    