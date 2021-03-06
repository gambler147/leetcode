class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            q, r = n//3, n%3
            if r > 1:
                return False
            n = q
        return True
    