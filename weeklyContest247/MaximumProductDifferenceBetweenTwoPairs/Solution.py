class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # first largest two and smallest 2
        nums.sort()
        return nums[-1]*nums[-2]-nums[0]*nums[1]
    
            