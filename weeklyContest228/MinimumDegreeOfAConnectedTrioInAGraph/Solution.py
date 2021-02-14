class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # first find all trios, then count number of nodes that
        # connect to these three nodes in the trio
        graph = collections.defaultdict(set) # use a map of set to record the graph edges
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # number of edges starting from each edge
        d = [0] + [len(graph[i]) for i in range(1,n+1)]
        
        # iterate all pairs of trios
        visited = set() # visited nodes
        res = float('inf')

        # iterate all nodes to find all trios
        for i in range(1,n+1):
            for j in graph[i]:
                for k in graph[j]:
                    if k in graph[i]:
                        res = min(res, d[i] + d[j] + d[k] - 6)
                        # remove i from k in case of duplicate counting
                        if i in graph[k]:
                            graph[k].remove(i)
                # remove j from graph[i] in case of duplicate counting
                if i in graph[j]:
                    graph[j].remove(i)
                
        return res if res != float('inf') else -1

        