class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while target > 1:
            if maxDoubles == 0:
                cnt += target-1
                break
            if target%2 == 0:
                cnt += 1
                target //= 2
                maxDoubles-=1
            else:
                cnt += 1
                target -= 1
        return cnt
    
