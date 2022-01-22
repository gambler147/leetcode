class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort descendingly; take every third candy for free. O(nlogn)
        cost.sort(reverse=True)
        res = 0 
        for i in range(len(cost)):
            if i%3==2:
                continue
            res += cost[i]
        return res
    
