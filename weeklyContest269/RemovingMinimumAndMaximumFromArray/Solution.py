class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        imin, imax = -1, -1
        vmin, vmax = 10**5, -10**5
        for i in range(n):
            if nums[i] <= vmin:
                imin, vmin = i, nums[i]
            if nums[i] >= vmax:
                imax, vmax = i, nums[i]
        
        a, b = min(imin, imax), max(imin, imax)
        return min(b+1, n - a, a+1 + n-b)
