class Solution:
    def minOperations(self, s: str) -> int:
        # count number of 1s and 0s in odd and even positions
        cnt = [[0, 0],[0, 0]]
        for i, c in enumerate(s):
            c = int(c)
            cnt[i%2][c] += 1
        return min(cnt[0][1]+cnt[1][0], cnt[0][0]+cnt[1][1])
    