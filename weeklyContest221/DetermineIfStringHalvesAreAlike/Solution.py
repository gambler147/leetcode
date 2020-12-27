class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        h1, h2 = 0, 0
        n = len(s)
        for i in range(n//2):
            if s[i] in vowels:
                h1 += 1
    
        for i in range(n//2, n):
            if s[i] in vowels:
                h2 += 1
        
        return h1 == h2
    