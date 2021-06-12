class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # conver to set
        total = set()
        for l, r in ranges:
            total.update(range(l,r+1))
        
        for v in range(left, right+1):
            if v not in total:
                return False
        return True
    