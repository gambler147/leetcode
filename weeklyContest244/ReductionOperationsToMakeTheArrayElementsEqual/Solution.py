class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        cnt = sorted([list(l) for l in cnt.items()], key=lambda x: x[0])
        # loop until one left
        res = 0
        while len(cnt) > 1:
            k, c = cnt.pop()
            res += c
            cnt[-1][1] += c
        return res
    