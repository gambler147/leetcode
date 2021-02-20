class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # KMP, greedy
        def findSubarray(nums, group, i):
            # find first index that the following subarray matches given group
            # the index starts from i in the nums array
            prefixTable = createPrefixTable(group)
            j = 0 # index in group
            while i < len(nums) and j < len(group):
                if nums[i] == group[j]:
                    i+=1
                    j+=1
                elif j!=0:
                    j = prefixTable[j-1]
                else:
                    i += 1
                if j == len(group):
                    return i - len(group)
            return -1
            
            
        def createPrefixTable(group):
            # KMP table
            n = len(group)
            table = [0 for _ in range(n)]
            l, r = 0, 1
            while r < n:
                if group[l] == group[r]:
                    table[r] = table[l] + 1
                    l += 1
                    r += 1
                elif l!= 0:
                    l = table[l-1]
                else:
                    r += 1
            return table
                    
        i = 0
        for g in groups:
            idx = findSubarray(nums, g, i)
            if idx == -1:
                return False
            i = idx + len(g)
        return True
    