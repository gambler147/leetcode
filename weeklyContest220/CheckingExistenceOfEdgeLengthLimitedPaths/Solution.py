class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # union find and sort queires by distance
        new_queries = sorted([(i, v) for i,v in enumerate(queries)], key=lambda x: x[1][2])
        edgeList.sort(key = lambda x: x[2])
        
        union = {} # start with each node given distance infinity and each in their own group
        for i in range(n):
            union[i] = i
            
        def find(x):
            # find root of x in union
            if union[x] != x:
                union[x] = find(union[x])
                return union[x]
            return x
        
        def merge(x, y):
            # merge x and y in union
            root_x = find(x)
            root_y = find(y)
            union[root_x] = union[root_y]
            
        # now we iterate queries and check whether given distance, pi and qi are in same union
        # iterage edgeList
        i = 0
        res = [None for _ in range(len(queries))]
        for j, (p, q, dist) in new_queries:
            while i < len(edgeList) and edgeList[i][2] < dist:
                x, y = edgeList[i][0], edgeList[i][1]
                merge(x,y)
                i+=1
            res[j] = True if find(p) == find(q) else False
        return res
                