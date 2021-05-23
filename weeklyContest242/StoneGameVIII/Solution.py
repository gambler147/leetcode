class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        """
        Let i be the index first player chooses to merge, 0-i stones will be merged. Then the score he got is
        prefix[0:(i+1)]. Define dp[i] is the optimal score play can get starting from index i. So we have
        dp[i] = max(prefix[j] - dp[j] for j > i)
        """
        n = len(stones)
        prefix = list(itertools.accumulate(stones))
            
        res = prefix[-1]
        for i in range(n-2, 0, -1):
            tmp = prefix[i] - res
            res = max(res, tmp)
        return res
    