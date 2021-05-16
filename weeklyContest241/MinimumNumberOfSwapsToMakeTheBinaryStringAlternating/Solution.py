class Solution:
    def minSwaps(self, s: str) -> int:
        """
        count 1s and 0s in even and odd positions. Swap even 1s with odd 0s or swap even 0s with odd 1s.
        So if the occurences of even 1s == odd 0s or even 0s == odd 1s, the answer exists, and we return
        the smallest answer if both true.
        """
        n = len(s)
        cnt = [[0,0], [0,0]]
        for i in range(n):
            cnt[i%2][int(s[i])] += 1
        # check even 1s and odd 0s
        res = float('inf')
        if cnt[0][1] == cnt[1][0]:
            res = min(res, cnt[0][1])
        # check even 0s and odd 1s
        if cnt[0][0] == cnt[1][1]:
            res = min(res, cnt[0][0])
        
        return res if res != float('inf') else -1
    