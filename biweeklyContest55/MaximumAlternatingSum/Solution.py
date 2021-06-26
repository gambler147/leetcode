class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # dp. 
        # Dynamically keeping track of even number and odd number of alternating sum.
        # For a new element, update max_even and max_odd by (max_odd - num), (max_even+num) if 
        # the latter is greater
        # time O(n), space O(1)
        
        n = len(nums)
        max_even, max_odd = -float('inf'), -float('inf')
        for i in range(n):
            ans = nums[i]
            max_even, max_odd = max(max_even, max_odd - nums[i]), max(max_odd, max_even+nums[i], nums[i])
        return max(max_even, max_odd)
