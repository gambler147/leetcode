class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # find indices where nums[i] >= nums[i+1]. The maximum inconsistent number of indices can be 1
        n = len(nums)
        idx = -1
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                if idx != -1:
                    return False
                idx = i
        # check if nums[idx-1] < nums[idx+1] or nums[idx] < nums[idx+2]
        return (idx==-1) or (idx == 0 or nums[idx-1] < nums[idx+1]) or (idx==n-2 or nums[idx] < nums[idx+2])
       