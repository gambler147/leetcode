class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        from sortedcontainers import SortedList
        # sort queries and rooms by the size decreasingly, 
        # for each query, add all rooms whose size >= query_size to a sorted list (self-balancing binary search tree),
        # then use binary search to find the closest roomid.
        # Time complexity: O(klogk + nlogn), where k is the query length and n is the rooms length
        queries = sorted(enumerate(queries), key=lambda x: -x[1][1])
        # sort rooms by size decreasing first
        rooms.sort(key=lambda x: -x[1])
        
        res = [None for _ in range(len(queries))]
        j = 0 # index in rooms
        tree = SortedList()
        
        # print(queries, rooms)
        for i, (preferred, minSize) in queries:
            while j < len(rooms) and rooms[j][1] >= minSize:
                # add valid rooms to the tree
                tree.add(rooms[j][0])
                j+=1
            # find id
            if len(tree) == 0:
                res[i] = -1
                continue
            idx = tree.bisect_left(preferred)
            # compare idx and idx-1 (if either exists)
            if idx == len(tree) or (idx - 1 >= 0 and abs(tree[idx-1] - preferred) <= abs(tree[idx] - preferred)):
                res[i] = tree[idx-1]
            else:
                res[i] = tree[idx]
        return res
                        