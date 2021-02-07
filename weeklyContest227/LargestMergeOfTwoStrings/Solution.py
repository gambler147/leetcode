class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # greedy O(n^2)
        res = []
        n1, n2 = len(word1), len(word2)
        i, j = 0,0
        while i < n1 and j < n2:
            if word1[i] > word2[j]:
                res.append(word1[i])
                i += 1
            elif word1[i] < word2[j]:
                res.append(word2[j])
                j += 1
            else:
                # word1[i] == word2[j]
                if word1[i:] >= word2[j:]:
                    res.append(word1[i])
                    i += 1
                else:
                    res.append(word2[j])
                    j += 1
        
        if i < n1:
            res.extend(list(word1[i:]))
        
        if j < n2:
            res.extend(list(word2[j:]))
            
        return ''.join(res)
    