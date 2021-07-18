class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # dp
        m, n = len(points), len(points[0])
        cur = points[0]
        for i in range(1, m):
            cur = self.dp(cur, points[i])
        return max(cur)
    
    def dp(self, cur, nxt):
        n = len(cur)
        # pre compute lmax_idx and rmax_idx array where 
        # lmax_idx is defined as lmax_idx[i] = argmax(l[j] + j, j<=i)
        # rmax_idx is defined as rmax_idx[j] = argmax(r[j] - j, j>=i)
        lmax_idx, rmax_idx = [0] * n, [n-1]*n
        l = [cur[j]+j for j in range(n)]
        r = [cur[j]-j for j in range(n)]
        for i in range(1,n):
            lmax_idx[i] = i if l[i] >= l[lmax_idx[i-1]] else lmax_idx[i-1]
        for i in range(n-2,-1,-1):
            rmax_idx[i] = i if r[i] >= r[rmax_idx[i+1]] else rmax_idx[i+1]
        res = [max(cur[lmax_idx[i]] - abs(i-lmax_idx[i]), cur[rmax_idx[i]] - abs(i-rmax_idx[i])) + nxt[i] for i in range(n)]
        return res
            
        
