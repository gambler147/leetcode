class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []
        for i in range(n):
            if i%k == 0:
                res.append(s[i])
            else:
                res[-1] += s[i]
        
        if len(res[-1]) < k:
            res[-1] = res[-1] + fill*(k-len(res[-1]))
        return res
    
