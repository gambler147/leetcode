class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        sort and match largest numbers to smallest numbers. We can prove for other assignments, the maximum is
        always larger than proposed assignment.
        """
        n = len(nums)
        nums.sort()
        max_pair_sum = -float('inf')
        for i in range(n//2):
            max_pair_sum = max(max_pair_sum, nums[i] + nums[n-i-1])
        return max_pair_sum
    