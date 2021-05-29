class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Solution 2: dp with bitmask. Time complexity: O(n*2^n)
        """
        n = len(nums1)
        @functools.lru_cache(None)
        def dp(i, mask):
            if i == n:
                return 0
            # loop through all j that has not been paired
            ans = float('inf')
            for j in range(n):
                if mask & (1 << j):
                    ans = min(ans, dp(i+1, mask - (1<<j)) + (nums1[i] ^ nums2[j]))
            return ans
        return dp(0, (1<<n)-1)
    