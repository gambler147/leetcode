class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        
        # greedy. 
        # It is always good to start from the smallest even to largest
        # whenever the remainder is smaller or equal than the sum of previous even intergers, we stop
        # the goal is to find max even 2k, such that finalSum - ( 2 + 4 + .. + 2k ) > 2k
        # <=> k(1+k) + 2k < finalSum
        # binary search
        i,j = 0, finalSum
        while i < j:
            m = (i+j+1) >> 1
            if m*(m+1) + 2*m >= finalSum:
                j = m-1
            else:
                i = m
                
        res = [2*i for i in range(1,i+1)]
        return res + [finalSum - sum(res)]
    
