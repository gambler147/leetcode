class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # sort by arriving times. Use a heap to store leaving times
        # O(nlogn)
        
        times = sorted(enumerate(times), key=lambda x: x[1])
        n = len(times)
        occupied = {} # map from friend index to position
        leaving = [] # heap
        avail = [] # avail chairs
        for i in range(n):
            heapq.heappush(avail, i)
            
        for i, (a, l) in times:
            # unoccupy chairs for leaving times less than current time
            while leaving and leaving[0][0] <= a:
                _, j = heapq.heappop(leaving)
                chair = occupied.pop(j)
                heapq.heappush(avail, chair)
            
            # assign chair to friend i
            chair = heapq.heappop(avail)
            if targetFriend == i:
                return chair
            occupied[i] = chair
            heapq.heappush(leaving, (l, i))
        return
    
