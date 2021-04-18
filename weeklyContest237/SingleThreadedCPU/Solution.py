class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # use a min-heap, (processing time, index)
        tasks = sorted([(i, v) for i,v in enumerate(tasks)], key=lambda x: (x[1][0], x[0]))
        # print(tasks)
        h = []
        res = []
        cur,i = 0, 0
        while i < len(tasks):
            # et, pt = tasks[i]
            if h:
                pt, j = heapq.heappop(h)
                cur += pt
                res.append(j)
            
            else:
                cur = tasks[i][1][0]
                
            while i < len(tasks) and tasks[i][1][0] <= cur:
                heapq.heappush(h, (tasks[i][1][1], tasks[i][0]))
                i+=1
        
        while h:
            pt, j = heapq.heappop(h)
            res.append(j)
        return res
        
            
        