class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ctr_a = collections.Counter(a)
        ctr_b = collections.Counter(b)
        na, nb = len(a), len(b)
        
        res = float('inf')
        # prefix sum
        prefix_a = [0 for _ in range(26)]
        prefix_a[0] = ctr_a['a']
        prefix_b = [0 for _ in range(26)]
        prefix_b[0] = ctr_b['a']
        for i in range(1,26):
            prefix_a[i] = prefix_a[i-1] + ctr_a[chr(ord('a')+i)]
            prefix_b[i] = prefix_b[i-1] + ctr_b[chr(ord('a')+i)]
        
        # condition 1 and 2
        for i in range(25):
            res = min(res, na-prefix_a[i]+prefix_b[i], nb-prefix_b[i]+prefix_a[i])
        
        # condition 3
        for i in range(26):
            c = chr(ord('a')+i)
            res = min(res, na-ctr_a[c] + nb-ctr_b[c])
            
        return res
    
            