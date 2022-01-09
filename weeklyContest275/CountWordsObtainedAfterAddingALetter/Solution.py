class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # sort each word in start words and target words
        # construct a set for start words. Check for each target words if in the start words set
        # O((m + n)*26log(26))
        s = set([''.join(sorted(w)) for w in startWords])
        res = 0
        for t in targetWords:
            l = len(t)
            for i in range(l):
                tmp = t[:i] + t[i+1:]
                if ''.join(sorted(tmp)) in s:
                    res += 1
                    break
        return res
    
