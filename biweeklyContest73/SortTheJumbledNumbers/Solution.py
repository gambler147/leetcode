class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        values = []
        for v in nums:
            res = []
            strv = str(v)
            for s in strv:
                res.append(str(mapping[int(s)]))
            values.append(int( ''.join(res)) )
        
        zipped = zip(nums, values)
        
        ans = sorted(zipped, key = lambda x: x[1])
        return [v[0] for v in ans]
    
    
