class Solution:
    def maximumTime(self, time: str) -> str:
        l = [c for c in time]
        if l[0]=='?': l[0]='2' if l[1] in '0123?' else '1'
        if l[1]=='?': l[1]='3' if l[0]=='2' else '9'
        if l[3]=='?': l[3]='5'
        if l[4]=='?': l[4]='9'
        return ''.join(l)
             