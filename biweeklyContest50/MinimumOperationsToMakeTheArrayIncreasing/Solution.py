class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cur = -float('inf')
        res = 0
        for n in nums:
            if n > cur:
                cur = n
                continue
            else:
                res += cur+1 - n
                cur+=1
        return res
    