class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        # the arr is grouped by i mod k. There are in total k groups.
        # for each such group, this is equivalent of finding the longest non-decreasing subsequence
        from bisect import bisect_right
        n = len(arr)
        res = 0
        for i0 in range(k):
            stack = []
            for i in range(i0, n, k):
                stack.append(arr[i])
            m = len(stack)
            # find the longest non-decreasing subsequence
            longest = self.longestNonDecreasingSubsequence(stack)
            res += m-longest
        return res
            
    def longestNonDecreasingSubsequence(self, arr):
        n = len(arr)
        res = []
        for a in arr:
            i = bisect_right(res, a)
            if i == len(res):
                res.append(a)
            else:
                res[i] = a
        return len(res)
        
