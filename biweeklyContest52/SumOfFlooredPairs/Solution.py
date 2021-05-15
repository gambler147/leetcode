class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        # We first sort values in nums array. Then for each number a
        # we look for numbers b such that floor(b/a) == m.
        # So use a prefix counter, prefix[k] is the total number of elements who are smaller or equal
        # than k, then for a given multiple m, number of elements b with floor(b/a) == m is prefix[m*a-1] - prefix[a-1].
        # We iterate a from 1 to MAX(nums), we increase m from 1 up until MAX/a (a*m <= MAX).

        # Time complexity: O(nlogn + MlogM) (sorting + looping), where n is the size of nums and M is the maximum value
        # in array. Since in the loop computing all possible multiples m from 1 upto M, each loop needs and operation number
        # is M/m, so total operations are M + M/2 + ... M/M = M(1 + 1/2 + .. +1/M) ~ MlogM
        
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        MAX = nums[-1]
        cnt = [0 for _ in range(MAX+1)]
        prefix = [0 for _ in range(MAX+1)]
        # initialized cnt and prefix
        for a in nums:
            cnt[a] += 1
        
        for i in range(1, MAX+1):
            prefix[i] = prefix[i-1] + cnt[i]
            
        res = 0
        for i in range(1, MAX+1):
            # pruning
            if prefix[i] == 0:
                continue
            for j in range(i, MAX+1, i):
                y = prefix[min(j+i-1, MAX)] - prefix[j-1]
                res += y * (j // i) * cnt[i]
        return res % MOD
            

        