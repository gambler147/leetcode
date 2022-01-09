class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # plant the plants with larget growTime
        # O(nlogn)
        order = sorted(enumerate(growTime), key = lambda x: -x[1])
        res = 0
        cur = 0
        for i, t in order:
            cur += plantTime[i]
            res = max(res, cur+t)
        return res
    
