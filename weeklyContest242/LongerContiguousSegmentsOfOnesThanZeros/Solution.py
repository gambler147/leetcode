class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = s.split("0")
        zeros = s.split("1")
        res = max(map(len, ones)) - max(map(len, zeros))
        return True if res > 0 else False
    