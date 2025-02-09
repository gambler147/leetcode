class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][x][y] is total number of substrings ending i 
        # with the number % x is y
        from collections import defaultdict
        n = len(s)
        dp = [defaultdict(int) for _ in range(10)]        
        res = 0
        
        for i in range(n):
            v = int(s[i])
            for x in range(1, 10):
                new_dp = defaultdict(int)
                new_dp[v % x] += 1
                
                for y in dp[x]:  # Only iterate over nonzero entries
                    new_dp[(10 * y + v) % x] += dp[x][y]

                dp[x] = new_dp  # Update the dp state
            res += dp[v][0]

        return res

