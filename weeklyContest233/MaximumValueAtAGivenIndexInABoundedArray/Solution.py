class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # we can use binary search to find the maximum value of nums[index]
        # for each given nums[index] = x, we check the minimum sum needed to satisfy the condition
        def helper(x):
            # return true if nums[index] = x meets the condition
            # for either half side of array, need to find number of jumps needed
            # to reach x, and need to compare number of jumps agains subarray size
            def findSum(v, s):
                # s is the size of array, v is the maximum value we want to achieve
                jumps = v - 1
                if jumps > s:
                    # the starting point is not 1 anymore
                    return (2*v-s+1)*s // 2
                else:
                    # starting point is 1, and just need to count number of jumps
                    return s + (1+jumps)*jumps // 2
            
            return findSum(x, index+1) + findSum(x, n-index) - x <= maxSum
            
        l,r = 1, maxSum
        while l < r:
            m = (l+r+1)>>1
            if helper(m):
                l = m
            else:
                r = m-1
        return l
                