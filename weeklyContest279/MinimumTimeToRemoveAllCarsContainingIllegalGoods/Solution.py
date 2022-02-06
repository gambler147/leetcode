class Solution:
    def minimumTime(self, s: str) -> int:
        # dynamic programming. O(n)
        # dp_l[i], minimum time to remove all illegal cars from the left for index 0 to i
        # dp_r[i], minimum time to remove all illegal cars from the right for index i to n-1
        if s == '0':
            return 0
        n = len(s)
        dp_l = [n for _ in range(n)]
        dp_r = [n for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp_l[i] = s[i] == '1'
                continue
            
            if s[i] == '0':
                dp_l[i] = dp_l[i-1]
            else:
                dp_l[i] = min(i+1, dp_l[i-1] + 2)
                
        for i in range(n-1,-1,-1):
            if i == n-1:
                dp_r[i] = s[i] == '1'
                continue
            
            if s[i] == '0':
                dp_r[i] = dp_r[i+1]
            else:
                dp_r[i] = min(n-i, dp_r[i+1] + 2)
                
        res = n
        for i in range(n-1):
            res = min(res, dp_l[i] + dp_r[i+1])
            
        return res
    
