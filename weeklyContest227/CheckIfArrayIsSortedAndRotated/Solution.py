class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                cnt += 1
                if cnt > 1:
                    return False
        if nums[-1] > nums[0]:
            cnt += 1
            if cnt > 1:
                return False
        return True
    