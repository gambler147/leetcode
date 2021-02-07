class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # split nums into two half subarrays and find all subset sums (s1, s2) in each half. O(2^(n/2))
        # then we sort both subset sums, and try to find
        # a in s1, b in 2 such that a+b is closest to t. o(2^(n/2) * log(2^(n/2))) for this step
        # Total time complexity o(2^(n/2) * log(2^(n/2)))
        n = len(nums)
        sum1 = set()
        sum1.add(0)
        for i in range(n//2):
            tmp = set()
            for s in sum1:
                tmp.add(s)
                tmp.add(s+nums[i])
            sum1 = tmp
        
        sum2 = set()
        sum2.add(0)
        for i in range(n//2, n):
            tmp = set()
            for s in sum2:
                tmp.add(s)
                tmp.add(s+nums[i])
            sum2 = tmp
        
        # find s1 in sum1, s2 in sum2, s1+s2 closest to goal
        sum1 = sorted(sum1)
        sum2 = sorted(sum2)
        i, j = 0, len(sum2)-1
        res = abs(goal)
        while i < len(sum1) and j >= 0:
            cur = sum1[i] + sum2[j] - goal
            res = min(res, abs(cur))
            if cur > 0:
                j-=1
            else:
                i+=1
        return res
    