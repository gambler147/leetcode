class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # rolling window
        n = len(nums)
        s = 0
        res = [-1 for _ in range(n)]
        for i in range(n):
            s += nums[i]
            if i - 2*k >= 0:
                res[i-k] = s//(2*k+1)
                s -= nums[i-2*k]
        return res
