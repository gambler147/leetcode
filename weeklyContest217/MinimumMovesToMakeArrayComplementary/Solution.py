class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # use array to record changes when we move from target of m to m+1
        n = len(nums)
        tmp = [0 for _ in range(2*limit+2)]
        for i in range(n//2):
            l,r = nums[i], nums[n-i-1]
            tmp[2] += 2
            tmp[min(l,r)+1] -= 1
            tmp[l+r] -= 1
            tmp[l+r+1] += 1
            tmp[max(l,r)+limit+1] += 1
            
        res = float('inf')
        cur = 0
        for v in range(2, 2*limit+1):
            cur += tmp[v]
            res = min(cur, res)
            
        return res