class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # convert LCS to LIS
        # first find indices in arr such that target[i] == arr[j]
        # initialize an array A, append i to A
        pos = {v: idx for idx, v in enumerate(target)}
        A = []
        for a in arr:
            if a in pos:
                A.append(pos[a])
        # now the problem becomes finding the longest increasing subsequence
        res = []
        for a in A:
            i = bisect.bisect_left(res, a)
            if i == len(res):
                # largest element, append it to the end
                res.append(a)
            else:
                # found a smaller number in index i, could replace res[i] with it
                res[i] = a
        return len(target) - len(res)
    
