class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # use additional array as sorted nums1, then for each pair a,b in nums1, nums2
        # binary search b in nums1
        n1_sorted = sorted(nums1)
        total = 0
        max_imp = 0
        for a,b in zip(nums1,nums2):
            total += abs(a-b)
            l = bisect.bisect_left(n1_sorted, b)
            if l < len(nums1):
                max_imp = max(max_imp, abs(a-b) - abs(n1_sorted[l] - b))
            if l > 0:
                max_imp = max(max_imp, abs(a-b) - abs(n1_sorted[l-1] - b))
        return (total - max_imp) % (10**9+7)
    