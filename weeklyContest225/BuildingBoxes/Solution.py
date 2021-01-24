class Solution:
    def minimumBoxes(self, n: int) -> int:
        # first construct perfect pyramid with k levels 
        # which means finding a k, such that k*(k+1) >= n.
        # Then we remove boxes until number of boxes is equal or smaller than n.
        base = 0
        row = 0
        total = 0
        while n > total:
            row += 1
            base += row
            total += base

        # remove
        while total > n:
            base -= 1
            total -= row
            row -= 1
            if total < n: return base+1
        return base
    