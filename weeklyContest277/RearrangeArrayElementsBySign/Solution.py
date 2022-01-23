class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for v in nums:
            if v > 0:
                pos.append(v)
            else:
                neg.append(v)
                
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res
    
