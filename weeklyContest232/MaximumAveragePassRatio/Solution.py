class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # if we assign k extraStudents to classes[i], lets say classes[i] = [a,b]
        # the improvement of each extraStudent for the total ratio is (b-a)/(b*(b+1))
        # so we can maintain a max heap and put [(b-a)/(b*(b+1)), a, b] in the heap and 
        # each time we pop one with maximum ratio and update it to the heap
        # total time complexity O(nlogn + e), space complexity O(n), where n is the number of
        # classes and e is number of extra students
        n = len(classes)
        h = []
        for a, b in classes:
            heapq.heappush(h, (-(b-a)/(b*(b+1)), a, b))
        
        # loop through extra students
        for _ in range(extraStudents):
            r, a, b = heapq.heappop(h)
            a, b = a+1, b+1
            heapq.heappush(h, (-(b-a)/(b*(b+1)), a, b))
            
        # calculate average passing ratio
        s = 0
        while h:
            r, a, b = heapq.heappop(h)
            s += a/b
        return s/n
        