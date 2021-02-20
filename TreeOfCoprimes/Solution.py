class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # since the value of nodes range from 0 to 50,
        # we can use dfs, and record a map of value -> list((node, depth)) 
        # and for each child node, we go through all values in the map
        # and find the closest node that is coprime to current node
        n = len(nums)
        # construct graph
        graph = collections.defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        res = [-1 for _ in range(n)]
        visited = set()
        def dfs(i, mp, lvl):
            visited.add(i)
            # mp is the map of val -> list(nodes)
            # function finds the closest node whose value coprimes with current node's value
            val = nums[i]
            max_lvl = -1 # set a big number for the closest node level that coprimes
            for v in mp.keys():
                if len(mp[v]) > 0 and gcd(val, v) == 1:
                    # last node in mp[v] is the answer, check if the node's level is higher than the rest
                    if mp[v][-1][1] > max_lvl:
                        res[i] = mp[v][-1][0]
                        max_lvl = mp[v][-1][1]
            # add ith node value to mp
            mp[val].append((i, lvl))
            # go through i's child nodes
            for j in graph[i]:
                if j not in visited:
                    dfs(j, mp, lvl+1)
            # pop ith node
            mp[val].pop()
                
        def gcd(x, y):
            x,y = min(x,y), max(x,y)
            while x >= 1:
                x, y = y%x, x
            return y
        
        dfs(0, collections.defaultdict(list), 0)
        return res
        