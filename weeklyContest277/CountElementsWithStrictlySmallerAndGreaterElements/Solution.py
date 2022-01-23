class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        while i < n and nums[i] == nums[0]:
            i += 1
        
        j = n-1
        while j >= 0 and nums[j] == nums[n-1]:
            j -= 1
        
        return max(0, j - i + 1)
    
