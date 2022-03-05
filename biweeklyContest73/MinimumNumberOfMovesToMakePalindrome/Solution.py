class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # Greedy, O(n^2)
        s = list(s)
        n = len(s)
        
        count = 0
        l,r = 0,n-1
        while l < r:
            if s[l] != s[r]:
                k = r
                while k > l and s[k] != s[l]:
                    k -= 1
                if k == l:
                    count += 1
                    s[l], s[l+1] = s[l+1], s[l]
                else:
                    for j in range(k, r):
                        s[j], s[j+1] = s[j+1], s[j]
                        count += 1
                    l += 1
                    r -= 1
            else:
                l += 1
                r -= 1
            
        return count
        
