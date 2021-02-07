class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # greedy
        score = 0
        while True:
            a,b,c = sorted((a,b,c))
            if b <= 0:
                return score
            b-=1
            c-=1
            score+=1
