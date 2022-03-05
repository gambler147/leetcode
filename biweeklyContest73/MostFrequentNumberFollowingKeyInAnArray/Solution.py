class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = collections.Counter()
        for i in range(len(nums)-1):
            if key == nums[i]:
                cnt[nums[i+1]] += 1
        return max(cnt, key = lambda x: cnt[x])
    
