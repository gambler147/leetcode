class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        """
        Prefix sum + binary search + greedy
        
        Sort packges. Iterate and sort each list of boxes. Starting from the smallest box, determine if there
        are unpacked packages whose sizes are smaller or equal than current box size. If so, put them into 
        current box, then update index. 
        
        Use a prefix sum for packages to reduce computation. Use binary search in each iteration in boxes to find
        smaller packages. 
        
        Time complexity: O(nlogn+mlog(n)log(m)), space complexity O(n), where n is package size and m is total size of boxes
        """
        
        MOD = 10**9+7
        n = len(packages)
        m = len(boxes)
        packages.sort()
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + packages[i])
        # loop through each box list, find index i such that package[i] <= boxes[j]
        res = float('inf')
        for bxs in boxes:
            bxs.sort()
            i = 0 # start index in package
            waste = 0
            for b in bxs:
                j = bisect.bisect_right(packages, b)
                # if j == i, means there is no package fits box b
                waste += b*(j-i) - (prefix[j] - prefix[i])
                i = j

            if i < n: continue
            res = min(res, waste)
        return res%MOD if res != float('inf') else -1
                
            