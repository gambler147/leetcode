class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # find time needed for each pair of cars to colide, use a heap to record these cars
        # each time pop out a car and merge with the next car
        n = len(cars)
        res = [-1 for _ in range(n)]
        
        # use a linked list to keep track of cars' next car and previous car
        next_car = [i+1 for i in range(n)]
        next_car[-1] = -1
        prev_car = [i-1 for i in range(n)]
        prev_car[0] = -1
        
        timeh = []  # heap to record time needed for collision
        for i in range(n-1):
            if cars[i][1] > cars[i+1][1]:
                heapq.heappush(timeh, ((cars[i+1][0]-cars[i][0]) / (cars[i][1] - cars[i+1][1]), i))
            
        # loop through the heap
        total_time_elapsed = 0
        while timeh:
            # pop out the first two cars that collide
            t, idx = heapq.heappop(timeh)
            # if idx has been updated, we pass
            if res[idx] != -1:
                continue
            # record time for this car to collide
            res[idx] = t
            # note that the next car's speed is not changing, we only need to update time needed for prevous
            # car to collide 
            pcar = prev_car[idx]
            ncar = next_car[idx]
            prev_car[ncar]=pcar
            # update prevous_car's next index
            if pcar != -1:
                next_car[pcar] = ncar
                # note that all cars has run for t seconds, so we can find pcar's position since pcar has not collide 
                # with next car yet, similarly we can know ncar's position, we can easily find additional time needed
                # for pcar to collide into ncar
                # add to heap if pcar speed > ncar speed
                if cars[pcar][1] > cars[ncar][1]:
                    pcar_pos = t * cars[pcar][1] + cars[pcar][0]
                    ncar_pos = t * cars[ncar][1] + cars[ncar][0]
                    pcar_t = t + (ncar_pos-pcar_pos) / (cars[pcar][1] - cars[ncar][1])
                    heapq.heappush(timeh, (pcar_t, pcar))
                    
        return res
    