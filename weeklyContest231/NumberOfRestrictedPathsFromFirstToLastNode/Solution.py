class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9+7
        distanceToLastNode = [float('inf') for _ in range(n+1)]
        graph = collections.defaultdict(set)
        weights = {}
        for u,v,w in edges:
            graph[u].add((v,w))
            graph[v].add((u,w))
            
        # Djikstra
        frontier = [(0, n)]
        visited = set(frontier)
        while frontier:
            dist, node = heapq.heappop(frontier)
            visited.add(node)
            if dist >= distanceToLastNode[node]:
                continue
            distanceToLastNode[node] = dist
            # loop its neighbors
            for (u, w) in graph[node]:
                if u not in visited:
                    heapq.heappush(frontier, (w+dist, u))
        
        # Djikstra again
        num_paths = [0 for _ in range(n)] + [1]
        bfs = [(0,n)]
        visited = set(bfs)
        while bfs:
            dist, node = heapq.heappop(bfs)
            if node in visited:
                continue
            visited.add(node)
            for (u, w) in graph[node]:
                if u not in visited:
                    if distanceToLastNode[u] > distanceToLastNode[node]:
                        num_paths[u] += num_paths[node]
                        heapq.heappush(bfs, (distanceToLastNode[u], u))

        return num_paths[1] % MOD
                        
        