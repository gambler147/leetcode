class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            n = len(w)
            for i in range(n//2):
                if w[i] != w[n-i-1]:
                    break
            else:
                return w
        return ""
    
