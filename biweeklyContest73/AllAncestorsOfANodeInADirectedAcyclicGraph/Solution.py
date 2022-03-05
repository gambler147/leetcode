class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # reverse link and dfs O(n^2)
        link = collections.defaultdict( list )
        # build graph
        for f, t in edges:
            link[t].append(f)
            
        
        res = []
        # iterate
        for i in range(n):
            l = self.dfs(i, link)
            res.append(l)
            
        return res
        
    def dfs(self, node, link):
        # return the list of parents
        visited = set()
        cur = [node]
        while cur:
            tmp = set()
            for v in cur:
                # get all parents
                for par in link[v]:
                    if par in visited:
                        continue
                    # add to tmp set
                    tmp.add(par)
                    visited.add(par)
            cur = tmp
            
        return sorted(visited)
    
