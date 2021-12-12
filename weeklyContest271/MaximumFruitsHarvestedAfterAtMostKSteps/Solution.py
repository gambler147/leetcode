class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], p: int, k: int) -> int:
        # Two pointers. Keep track of current sum between the pointers O(n)
        
        n = len(fruits)
        # first find the leftmost index such that the person can reach, i.e. leftmost fruit's position within reach
        li = 0
        while li < n and fruits[li][0] < p-k:
            li += 1
            
        # The person can get all fruits between leftmost fruit within reach and 
        # fruits between the leftmost one and person's position.
        cur = 0
        ri = li # right pointer
        while ri < n and fruits[ri][0] <= p:
            cur += fruits[ri][1]
            ri += 1
            
        res = cur
        # extend the right pointer from ri to the end of fruits
        while ri < n:
            if fruits[ri][0] - p > k:
                break
            # check if we can include fruit[ri]
            # find the distance
            if fruits[ri][0] - fruits[li][0] + min(fruits[ri][0] - p, abs(p - fruits[li][0])) <= k:
                cur += fruits[ri][1]
                ri += 1
            else:
                cur -= fruits[li][1]
                li += 1
            res = max(cur, res)

        return res
    
