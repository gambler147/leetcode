class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # rolling window, keep track of '0' s for [i+minJump, i+maxJump]
        l = list(s)
        n = len(l)
        # initialization
        if l[-1] == '1':
            return False
        
        for j in range(1, minJump):
            l[n-1-j] = '1'
        
        zeros = 1 # last position
                
        # loop from n-maxJump-1 to 0
        for j in range(minJump, n):
            if l[n-1-j] == '0':
                if zeros <= 0:
                    l[n-1-j] = '1'
            # remove l[n-1-j + maxJump] if 0
            if n-1-j + maxJump < n and l[n-1-j+maxJump] == '0':
                zeros -= 1
            # include l[n-1-j] + minJump
            if l[n-1-j+minJump-1] == '0':
                zeros += 1
            # print(zeros, j)
        return l[0] == '0'
    