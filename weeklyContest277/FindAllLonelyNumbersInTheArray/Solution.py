class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        
        res = []
        keys = set(counter.keys())
        for v in counter.keys():
            if counter[v] == 1 and v-1 not in keys and v+1 not in keys:
                res.append(v)
                
        return res
    
