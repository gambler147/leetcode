class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        # two pointers and simulation. O(n)
        n = len(plants)
        i = 0 # j = n-1
        
        refill = 0
        curA, curB = capacityA, capacityB
        while i < n - i -1:
            if curA < plants[i]:
                curA = capacityA
                refill += 1
            curA -= plants[i]
            if curB < plants[n-i-1]:
                curB = capacityB
                refill += 1
            curB -= plants[n-i-1]
            i += 1
        
        if i == n-i-1:
            if plants[i] > max(curA, curB):
                refill += 1
        return refill
            
