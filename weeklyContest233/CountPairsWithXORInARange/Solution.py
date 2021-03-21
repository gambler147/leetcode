class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        # Trie
        # build a trie, from the leftmost bit to rightmost.
        # then we loop through every number b in nums, lets say the bits of nums is b1b2...bk
        # and the target value is x, with bits x1x2...xk
        # we loop i from 1 to k
        # if xi == 1, then we can add counts of numbers (a) whose ith bit == bi since the XOR makes 0 in ith bit 
        # thus b ^ a < x. If xi == 0, we goes down to the trie nodes where ith bits == big
        class Trie:
            def __init__(self):
                self.root = {}
                self.depth = 15 # 2**15 > 2*10**4
                
            def insert(self, val):
                node = self.root
                for i in reversed(range(self.depth)):
                    bit = (val >> i) & 1
                    if bit in node:
                        node[bit]['cnt'] += 1 
                    else:
                        node[bit] = {'cnt': 1}
                    node = node[bit]
                    
            def count(self, x, val):
                # find number of elements a such that a ^ x < val
                res = 0
                node = self.root
                for i in reversed(range(self.depth)):
                    if not node: break
                    bit = (val >> i) & 1
                    tmp = (x >> i) & 1
                    # check bit is 1 or 0
                    if bit:
                        # if bit is one, counter number of elements whose ith bit is tmp
                        if tmp in node:
                            res += node[tmp]['cnt']
                        node = node.get(1-tmp, {})
                    else:
                        # if bit is zero, we have to let ith bit equal tmp
                        node = node.get(tmp, {})
                return res
            
        
        # count
        res = 0
        trie = Trie()
        for x in nums:
            res += trie.count(x, high+1) - trie.count(x, low)
            trie.insert(x)
        return res
