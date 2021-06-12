class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # module and prefix
        k = k%sum(chalk)
        n = len(chalk)
        for i in range(n):
            k -= chalk[i]
            if k < 0:
                return i
        
            
            