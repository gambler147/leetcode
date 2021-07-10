class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], fees: List[int]) -> int:
        n = len(fees)
        h = [] # min-heap to store (cost, time, city); will only push to heap if and edge does not increase time to exceed
        heapq.heappush(h, (fees[0], 0, 0))
        
        # build graph
        graph = collections.defaultdict(list)
        for x,y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))
        
        # optimal times of arriving each city
        times = {}
        
        # Dijkstra
        while h:
            cost, time, city = heapq.heappop(h)
            if time > maxTime:
                continue
                
            if city == n-1:
                return cost
            
            # only traverse from current city if city is not visited or time < current optimal time
            if city not in times or times[city] > time:
                times[city] = time
                # traverse its neighbors
                for c, t in graph[city]:
                    heapq.heappush(h, (cost+fees[c], time+t, c))
        return -1
            
