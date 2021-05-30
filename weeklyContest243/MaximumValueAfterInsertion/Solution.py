class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] != '-':
            # find first index i such n[i] < x
            for i in range(len(n)):
                if int(n[i]) < x:
                    break
            else:
                i+=1
            # insert into ith position
        else:
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    break
            else:
                i+=1
        n = n[:i] + str(x) + n[i:]
        return n
            