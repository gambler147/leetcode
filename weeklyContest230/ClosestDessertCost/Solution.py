class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # closest subset sum problem
        
        # find closest subset sum in toppingCosts * 2 to target - s
        # can simply use brute force, time complexity O(2^(2*m)) ~ 10**6
        subsets = set([0])
        toppingCosts *= 2
        for c in toppingCosts:
            tmp = set()
            for s in subsets:
                tmp.add(s)
                tmp.add(s+c)
            subsets=tmp
        # find closest subset sum
        res = float('inf')
        for s in subsets:
            for base in baseCosts:
                if abs(res - target) > abs(s+base-target) or (abs(res - target) == abs(s+base-target) and s+base < res):
                    res = s+base
        return res
            
        