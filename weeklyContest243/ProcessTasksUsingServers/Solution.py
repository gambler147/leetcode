class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        m = len(tasks)
        res = [0 for _ in range(m)]
        # min heap (avail_time, weight, index)
        avail = []
        # initialize
        for i in range(n):
            heapq.heappush(avail, (servers[i], i))
        
        busy = []
        carry = 0
        cur = 0 # current time
        
        j = 0
        while j < m:
            cur = max(cur, j) # current time
            # update busy server
            while busy and busy[0][0] <= cur:
                # free server
                t, i = heapq.heappop(busy)
                heapq.heappush(avail, (servers[i], i))
            # if no server available, update current time
            if len(avail) == 0:
                cur = busy[0][0]
                while busy and busy[0][0] <= cur:
                    # free server
                    t, i = heapq.heappop(busy)
                    heapq.heappush(avail, (servers[i], i))
            # get top server, if no server available, 
            while j < m and j <= cur and len(avail) > 0:
                w, i = heapq.heappop(avail)
                # assign this server to task j
                res[j] = i
                # update avail time
                t = cur + tasks[j]
                heapq.heappush(busy, (t,i))
                j += 1
        return res
    
        