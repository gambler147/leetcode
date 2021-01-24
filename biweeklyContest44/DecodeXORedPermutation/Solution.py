class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # find prefix encoded array under operation XOR,
        # so prefix[k] = i1 ^ i(k+1). Then we find XOR of the prefix array
        # we will get answer = i2^i3^...^in since n is odd, then we iterate 
        # encoded array again to retrieve perm array
        n = len(encoded)+1
        prefix = 0 # equals i1 ^ i(k+1)
        cur = 0 # equals pow(i1,k)^....^i(k+1)
        for e in encoded:
            prefix ^= e
            cur = cur ^ prefix
        
        total = 0
        for i in range(1, n+1):
            total ^= i
        
        tmp = cur ^ total # first element of perm
        perm = []
        perm.append(tmp)
        for e in encoded:
            tmp ^= e
            perm.append(tmp)
        
        return perm
    
        