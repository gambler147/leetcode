class Solution:
    def makeStringSorted(self, s: str) -> int:
        # notice that each operation is changing current string to the closest 
        # lexiographically smaller string
        # so we only need to find number of lexiographically smaller string 
        # from the end

        MOD = self.MOD = 10**9+7
        n = len(s)
        # use a counter to temporarily store occurences of characters
        cnt = [0] * 26
        res = 0
        for i in range(n-1,-1,-1):
            v = ord(s[i]) - ord('a')
            cnt[v] += 1
            # calculate total combinations, multinomial distribution
            comb = sum(cnt[:v]) * self.fmod(n-i-1)
            for i in range(26):
                comb = comb * self.inv(self.fmod(cnt[i])) % MOD
            res = (res + comb) % MOD
        return res
        
    @lru_cache(None)
    def fmod(self, k):
        # factorial k! % mod
        return 1 if k <= 1 else (self.fmod(k-1) * k) % self.MOD
    
    @lru_cache(None)
    def inv(self, k):
        # inverse modulo of k with repect to mod
        return pow(k, self.MOD-2, self.MOD)
    