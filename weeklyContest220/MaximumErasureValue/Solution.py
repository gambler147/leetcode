class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # rolling window, using set
        n = len(nums)
        seen = set()
        cur = 0
        res = 0
        i, j = 0, 0
        while j < n:
            while nums[j] in seen:
                seen.remove(nums[i])
                cur -= nums[i]
                i+=1
            seen.add(nums[j])
            cur += nums[j]
            res = max(res, cur)
            j+=1
        return res

