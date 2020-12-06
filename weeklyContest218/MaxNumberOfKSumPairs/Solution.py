class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        res = 0
        for num in nums:
            if counter[k-num] > 0:
                counter[k-num] -= 1
                res += 1
            else:
                counter[num]+=1
        return res
        