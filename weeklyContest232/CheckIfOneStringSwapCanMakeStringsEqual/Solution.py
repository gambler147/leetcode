class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # find mismatched indices
        mismatch = []
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                mismatch.append([c1,c2])
                if len(mismatch) > 2:
                    return False
                
        if not mismatch or (len(mismatch) == 2 and mismatch[0] == mismatch[1][::-1]):
            return True
        
        return False
                