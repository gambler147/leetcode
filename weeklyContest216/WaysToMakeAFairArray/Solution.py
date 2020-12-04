class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        lo, ro, le, re = 0, 0, 0, 0 # left odd sum, right odd sum, left even sum, right even sum
        for i in range(n):
            if (i&1):
                re += nums[i]
            else:
                ro += nums[i]
                
        # iterate
        res = 0
        for i in range(n):
            if (i&1):
                # even position
                re -= nums[i]
                if lo+re == le+ro:
                    res+=1
                le += nums[i]
            else:
                # odd position
                ro -= nums[i]
                if lo+re == le+ro:
                    res+=1
                lo += nums[i]
        return res