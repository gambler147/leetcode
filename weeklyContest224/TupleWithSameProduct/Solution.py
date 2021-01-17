class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # use a counter to keep track of number of pairs that have a same product
        cnt = collections.defaultdict(int) 
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                cnt[nums[i]*nums[j]] += 1
                
        for k, v in cnt.items():
            res += v*(v-1)*4
            
        return res
    