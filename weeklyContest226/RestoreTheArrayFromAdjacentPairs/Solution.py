class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # use hash map of counter record number of adjacent elements of each element
        # if there is an odd appearence of an element, the element should be at the end
        # if no odd appearence of any element, we can start with any element
        n = len(adjacentPairs) + 1
        adj = collections.defaultdict(list)
        for u,v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        res = []
        # find the head
        for k,l in adj.items():
            if len(l) == 1:
                res.append(k)
                res.append(l[0])
                break
        while len(res) < n:
            nxt = adj[res[-1]]
            nxt.remove(res[-2])
            res.append(nxt[0])
        return res
            
            
        