class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # find total difference for first element
        left = 0
        right = 0
        for i in range(n):
            right += nums[i] - nums[0]
            
        res = [left+right]
        # from i to i+1, left increase diff*left_num, right decrease diff * right_num
        for i in range(1, n):
            left += (nums[i] - nums[i-1])*i
            right -= (nums[i] - nums[i-1]) * (n-i)
            res.append(left + right)
        return res
        