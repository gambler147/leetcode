class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        # dfs
        from collections import defaultdict
        links = defaultdict(list)
        for i, j in edges:
            links[i].append(j)
            links[j].append(i)
            
        # dfs
        res = 0
        visited = set()
        def dfs(node):
            nonlocal res
            # return total number of childs
            visited.add(node)
            childs = links[node]
            counts = []
            for c in childs:
                if c not in visited:
                    ans = dfs(c)
                    counts.append(ans)
            # if all counts equal or empty, current node is a good node
            if len(set(counts)) <= 1:
                res += 1
            
            return sum(counts) + 1
        
        dfs(0)
        return res
           

