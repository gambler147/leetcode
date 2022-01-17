class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp O(n)
        n = len(questions)
        dp = [0 for _ in range(n+1)] # dp[i] is the maximum score, where ith question is answerable
        for i in range(n-1, -1,-1):
            dp[i] = max(dp[i+1], questions[i][0])
            if i+questions[i][1]+1 <= n:
                dp[i] = max(dp[i], questions[i][0] + dp[i+questions[i][1]+1])
        
        return dp[0]
    
