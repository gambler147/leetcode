class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # pefect matching problem. Hungarian Algorithm
        # Time complexity: O(n^3), space complexity: O(n^2)
        
        from scipy.optimize import linear_sum_assignment
        n = len(nums1)
        cost = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                cost[i][j] = nums1[i] ^ nums2[j]
        
        row_ind, col_ind = linear_sum_assignment(cost)
        res = 0
        for i,j in zip(row_ind, col_ind):
            res += cost[i][j]
        return res
    