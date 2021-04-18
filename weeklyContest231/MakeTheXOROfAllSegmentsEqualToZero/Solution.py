class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # notice that if we want XOR[0] == XOR[1] == .. == XOR[n-k] == 0
        # it indicates that nums[i] == nums[i+k] for all i
        # the problem is reduced to for j = 0 to k-1, for all i%k == j,
        # the changes needed is I - max(cnt[v] for v in nums[i])
        
        n = len(nums)
        cnts = [collections.Counter(nums[j] for j in range(i, n, k)) for i in range(k)]
        
        # the final list is a repeating array of size k, so we are picking k numbers from the cnts
        # two cases
        # 1. one number of the k is not from the cnts
        max_cnts = [max(cnts[i].values()) for i in range(k)]
        res = n - (sum(max_cnts) - min(max_cnts))
        
        # 2. all k numbers are from the cnts. 
        # we loop through k cnts. We maintain a counter of cur, cur[v] is the maximum number of elements in nums
        # which makes the current XOR sum equal to v
        cur = cnts[0]
        for i in range(1, k):
            tmp = collections.defaultdict(int)
            for u in cur:
                for v in cnts[i]:
                    w = u^v
                    tmp[w] = max(tmp[w], cur[u] + cnts[i][v])
            cur = tmp
        return min(res, n - cur[0])
            