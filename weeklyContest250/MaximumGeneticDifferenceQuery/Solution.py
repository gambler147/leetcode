class Trie:
    BITS = 18
    def __init__(self):
        self.root = {}
        
    def add(self, val):
        node = self.root
        for i in range(self.BITS, -1, -1):
            bit = (val >> i) & 1
            if bit not in node:
                node[bit] = [{}, 0] # node[0] is the children and node[1] is the count
            node[bit][1] += 1
            node = node[bit][0]

    def remove(self, val):
        node = self.root
        for i in range(self.BITS, -1, -1):
            bit = (val >> i) & 1
            node[bit][1] -= 1
            node = node[bit][0]
            
    def findMaxXOR(self, val):
        # return maximum xor with val
        node = self.root
        res = 0
        for i in range(self.BITS, -1, -1):
            bit = (val >> i) & 1
            if (1-bit) in node and node[1-bit][1] > 0:
                node = node[1-bit][0]
                res |= (1 << i)
            else:
                node = node[bit][0]
        return res
    
    

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        # trie and dfs
        n, m = len(parents), len(queries)
        queryByNodes = [[] for _ in range(n)]
        for i, (node, val) in enumerate(queries):
            queryByNodes[node].append([val, i])

        # build graph
        root = -1
        graph = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p==-1: 
                root=i
            else:
                graph[p].append(i)

        res = [0 for _ in range(m)]
        trie = Trie()
        # dfs
        def dfs(node):
            # add node value to trie
            trie.add(node)
            for val, i in queryByNodes[node]:
                res[i] = trie.findMaxXOR(val)
            # dfs nodes
            for child in graph[node]:
                dfs(child)
            trie.remove(node)
            
        dfs(root)
        return res
    
