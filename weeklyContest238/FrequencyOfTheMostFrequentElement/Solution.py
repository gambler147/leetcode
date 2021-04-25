class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Two pointers. Time: O(nlogn), Space: O(n)
        
        # We first sort the array.
        # for each index i, we try to find the longest index j <= i such that we can turn all numbers 
        # from j to i to nums[i] within k operations. Note that number of operations needed to convert
        # all numbers from j to i is nums[i] * (i-j+1) - sum(nums[j] : nums[i])
        # we can pre-calculate prefix sum for calculating the sum.
        # when i increases and old j is not satisfying the condition, we increase j until
        # the condition is satisfied again. 
        
        nums.sort()
        n = len(nums)
        # prefix sum
        prefix = [0 for _ in range(n+1)]
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        # find i,j such that nums[j] * (j-i+1) - (prefix[j] - prefix[i]) <= k, and j-i is maximized
        i, j = 0, 0
        res = 0
        for i in range(n):
            while j < i and  nums[i] * (i-j) - (prefix[i] - prefix[j]) > k:
                j+=1
            res = max(res, i-j+1)
        return res
        