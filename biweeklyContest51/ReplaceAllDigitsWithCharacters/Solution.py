class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(1, len(s), 2):
            res.append(s[i-1])
            res.append(chr(ord(s[i-1]) + int(s[i])))
        if len(s)%2 == 1: res.append(s[-1])
        return ''.join(res)
    