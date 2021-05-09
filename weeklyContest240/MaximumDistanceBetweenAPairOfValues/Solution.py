class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # two pointers
        n1, n2 = len(nums1), len(nums2)
        res = 0
        j = -1
        for i in range(n1):
            # update j
            while j+1 < n2 and nums2[j+1] >= nums1[i]:
                j+=1
            if i <= j: res = max(res, j-i)
            i += 1
        return res
        