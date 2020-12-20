class Solution:
    def reformatNumber(self, number: str) -> str:
        s = number.replace('-', '').replace(' ', '')
        
        l = list(s)
        n = len(l)
        k = n%3
        res = []
        for i in range(n-k):
            res.append(l[i])
            if i%3 == 2:
                res.append('-')
        if k == 0:
            res.pop()
        elif k == 1:
            # four digits
            res.pop()
            res.pop()
            res.append('-')
            res.extend(l[-2:])
        else: 
            #k == 2:
            # two digits
            res.extend(l[-2:])
        return ''.join(res)
            
