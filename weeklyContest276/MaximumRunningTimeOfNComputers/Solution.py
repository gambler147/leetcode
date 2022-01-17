class Solution:
    def maxRunTime(self, n: int, bat: List[int]) -> int:
        # referrence
        # https://leetcode.com/problems/maximum-running-time-of-n-computers/discuss/1692939/JavaC%2B%2BPython-Sort-Solution-with-Explanation-O(mlogm)
        bat.sort()
        s = sum(bat)
        while bat[-1] > s/n:
            n -= 1
            s -= bat.pop()
        return s//n
    
