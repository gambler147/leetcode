class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # greedy + two pointer (O(n))
        # initially set i = j = k
        # maintain the min value of current subarray nums[i:j+1]
        # move left pointer i to i-1 if nums[i-1] >= nums[i]
        # move right pointer j to j+1 if nums[j+1] >= nums[j]
        # if nums[i-1] < cur_min and nums[j+1] < cur_min: if nums[i-1] < nums[j+1], move j vice versa
        n = len(nums)
        i = j = k;
        cur_min = nums[k] # current min value in subarray nums[i:j+1]
        res = nums[k] # current maximum score
        while i > 0 or j < n-1:
            if i > 0 and nums[i-1] >= cur_min:
                i-=1
                res = max(res, (j-i+1)*cur_min)
                continue
            
            if j < n-1 and nums[j+1] >= cur_min:
                j+=1
                res = max(res, (j-i+1)*cur_min)
                continue
                
            # neither side has a free roll
            # check if i == 0 or j == n-1, then we have to move the pointer
            if i == 0:
                j+=1
                cur_min = nums[j]
                res = max(res, (j-i+1)*cur_min)
                continue
                
            if j == n-1:
                i-=1
                cur_min = nums[i]
                res = max(res, (j-i+1)*cur_min)
                continue
            
            # if i-1 and j+1 are both valid and nums[i-1] < cur_min and nums[j+1] < cur_min
            # we compare which one is bigger
            if nums[i-1] <= nums[j+1]:
                # move j
                j+=1
                cur_min = nums[j]
                res = max(res, (j-i+1)*cur_min)
            else:
                # move i
                i-=1
                cur_min = nums[i]
                res = max(res, (j-i+1)*cur_min)
            
        return res
    