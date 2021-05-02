class Solution:
    def splitString(self, s: str) -> bool:
        # brute force
        n = len(s)
        t = int(s)
        def dfs(i, prev):
            if i >= n and prev != t:
                return True
            
            for j in range(i, n):
                # check if current value is 1 smaller than previous
                cur = int(s[i:j+1])
                if prev is None or cur == prev-1:
                    if dfs(j+1, cur):
                        return True
            return False
        return dfs(0, None)
    