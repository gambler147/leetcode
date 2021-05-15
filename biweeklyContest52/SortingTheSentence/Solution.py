class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        n = len(l)
        res = ['' for _ in range(n)]
        for x in l:
            res[int(x[-1])-1] = x[:-1]
            
        return ' '.join(res)
    