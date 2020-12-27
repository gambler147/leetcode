class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # sort nums and queries
        # use a binary tree
        nums.sort()
        queries = sorted([[x, m, i] for i, (x,m) in enumerate(queries)], key = lambda x: x[1]) # sort by m
        res = [0 for _ in range(len(queries))]
        # construct the tree
        tree = {}
        j = 0 # index of tree
        for x, m, i in queries:
            while j < len(nums) and nums[j] <= m:
                # insert nums[j] to the tree
                node = tree
                for k in range(30, -1, -1):
                    d = (nums[j] & (1 << k)) >> k 
                    if d in node:
                        # go to next level
                        node = node[d]
                    else:
                        node[d] = {}
                        node = node[d]
                j += 1
            # find maximum xor with x in tree
            ans = 0
            node = tree
            if not tree:
                res[i] = -1
                continue
                
            for k in range(30, -1, -1):
                # compare digit
                dx = (x & (1 << k)) >> k
                # print(dx, k, dx in node)
                if 1-dx in node:
                    ans += (1<<k)
                    node = node[1-dx]
                else:
                    node = node[dx]
                    
            res[i] = ans
            
        return res
            

        
    