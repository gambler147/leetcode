class Solution:
    def minFlips(self, s: str) -> int:
        """
        use a counter to store number of 1s and 0s in odd and even positions. 
        Then do a second pass, for each interation, update counter: switch odd
        and even 0s and 1s. If the length of string is odd, the leading digit
        should be added to the even position and decreased from odd position.
        
        Time complexity O(n), space complexity O(1)
        """
        n = len(s)
        cnt = [[0,0], [0,0]]
        for i in range(n):
            cnt[i%2][int(s[i])] += 1
        # second pass
        res = float('inf')
        for i in range(n):
            res = min(res, cnt[0][0]+cnt[1][1], cnt[1][0]+cnt[0][1])
            # update cnt, switch odd and even position
            cnt[0], cnt[1] = cnt[1], cnt[0]
            if n%2 == 1:
                cnt[0][int(s[i])] += 1
                cnt[1][int(s[i])] -= 1
        return res
            
        