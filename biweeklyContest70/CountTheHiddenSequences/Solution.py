class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Try to find max difference of two elements O(n)
        vmax, vmin = 0, 0
        cur = 0
        for v in differences:
            cur += v
            vmax = max(vmax, cur)
            vmin = min(vmin, cur)
            
        return max(0, (1 + upper - lower) - (vmax - vmin))
    
