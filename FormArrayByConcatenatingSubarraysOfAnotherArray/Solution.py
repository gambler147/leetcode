class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # brute force
        ng = len(groups)
        (g, k) = (0, 0) # kth index and gth group
        i, j = 0, 0 # ith index in nums
        while g < ng:
            if k == len(groups[g]):
                # go to next group
                g+=1
                k=0
                i=j
            else:
                # check if index exceeds the nums list
                if j >= len(nums):
                    return False
                # check if nums[j] == groups[g][k]
                if nums[j] == groups[g][k]:
                    j += 1
                    k += 1
                else:
                    i += 1
                    j = i
                    k = 0
        return True
                    
        