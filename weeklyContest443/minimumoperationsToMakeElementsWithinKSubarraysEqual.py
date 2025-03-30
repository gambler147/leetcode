from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        # dp[i][j] is minimum number of operations ot make j subarrays equal within first i elements
        # dp[i][j] = min(dp[i-1][j], dp[i-x][j-1] + med(nums[i-x+1:i])

        n = len(nums)
        XISODD = x % 2 == 1
        
        # use 2 sorted list to calculate distance to median
        ops = [None] * n
        small, large = SortedList(), SortedList()
        ssum = 0
        lsum = 0

        for i, v in enumerate(nums):
            # add element to corresponding sorted list
            if not large or large[0] <= v:
                large.add(v)
                lsum += v
            else:
                small.add(v)
                ssum += v

            # remove old element from sorted list
            if i >= x:
                if nums[i-x] >= large[0]:
                    large.remove(nums[i-x])
                    lsum -= nums[i-x]
                else:
                    small.remove(nums[i-x])
                    ssum -= nums[i-x]
                    
            # rebalance small and large sorted list to make sure the 0 <= len(large) - len(small) <= 1
            while len(large) - len(small) > 1:
                val = large.pop(0)
                small.add(val)
                lsum -= val
                ssum += val
            while len(large) < len(small):
                val = small.pop()
                large.add(val)
                lsum += val
                ssum -= val

            if i >= x-1:
                ops[i-x+1] = lsum - ssum - XISODD * large[0]

                    
        dp = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]
        # initialize, 0 operations for 0 subarrays
        for i in range(n):
            dp[i][0] = 0

        for i in range(n+1):
            for j in range(1, k+1):
                if i >= x:
                    dp[i][j] = min(dp[i-1][j], dp[i-x][j-1] + ops[i-x] )
        
        return dp[n][k]


