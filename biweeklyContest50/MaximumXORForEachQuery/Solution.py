class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        cur = functools.reduce(lambda a,b : a^b, nums)
        res = []
        MAX = 2**maximumBit-1
        for i in range(len(nums)):
            res.append(cur^MAX)
            cur^=nums.pop()
        return res
        