class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # rolling window. O(n)
        n = len(nums)
        t = sum(nums) # total number of 0s, we need to find a window with size t that contains maximum 0s
        
        # initial window
        cur = sum(nums[:t])
        res = t - cur
        # rolling
        for i in range(n):
            cur += nums[(i+t)%n] # include right end
            cur -= nums[i] # remove left end
            res = min(res, t-cur)
        return res
    
