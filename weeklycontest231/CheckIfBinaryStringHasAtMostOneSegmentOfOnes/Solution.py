class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        seen = False
        for i in range(n):
            if s[i] == '1':
                if seen == False:
                    seen = True
                elif s[i-1] == '0':
                    return False
        return True
                    
                    