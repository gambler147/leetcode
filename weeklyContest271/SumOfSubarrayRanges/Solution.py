class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # O(n^2) rolling window to calculate max and min for subarrays ending at j
        n = len(nums)
        
        res = 0
        for j in range(n):
            _max = -float('inf')
            _min = float('inf')
            for i in range(j, -1, -1):
                _max = max(_max, nums[i])
                _min = min(_min, nums[i])
                res += _max-_min
        return res

