class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        cur, res = nums[0], nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cur += nums[i]
            else:
                cur = nums[i]
            res = max(res, cur)
        return res
    