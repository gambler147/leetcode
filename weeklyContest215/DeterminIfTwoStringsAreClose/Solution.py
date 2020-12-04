class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)
        
        if (set(c1.keys()) != set(c2.keys())): return False
        
        c1 = sorted(c1.values())
        c2 = sorted(c2.values())
        
        for v1,v2 in zip(c1,c2):
            if (v1 != v2):
                return False
            
        return True
