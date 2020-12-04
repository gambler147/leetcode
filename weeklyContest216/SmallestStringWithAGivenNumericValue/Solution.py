class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # start from the end
        l = []
        for i in range(n):
            if k >= n-i + 25:
                l.append('z')
                k -= 26
            elif k >= n-i:
                l.append(chr(ord('a') + k-(n-i)))
                k = n-i-1
        return ''.join(l[::-1])