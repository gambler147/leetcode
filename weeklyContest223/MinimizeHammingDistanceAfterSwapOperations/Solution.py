class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # use union find to construct an union of indices from source
        # then iterate for each element in source, check if given element
        # can be swapped to the index of same element in target
        # we need a set of dict to counter occurences of each element mapped 
        # to the same root in union
        n = len(source)
            
        # initialize union
        union = {}
        for i in range(n):
            union[i] = i
            
        # union find for allowedSwaps
        def find(x):
            if union[x] == x:
                return x
            union[x] = find(union[x])
            return union[x]
        
        def merge(x, y):
            # merge union of x and y
            root_x = find(x)
            root_y = find(y)
            union[root_y] = root_x
            
        for a,b in allowedSwaps:
            merge(a, b)
            
        # update union
        for i in range(n): find(i)
            
        # construct a dictionary of counter
        counter = collections.defaultdict(collections.Counter)
        for i,e in enumerate(source):
            counter[find(i)][e] += 1
            
        res = 0
        for i,e in enumerate(target):
            if counter[find(i)][e] > 0:
                counter[find(i)][e] -= 1
            else:
                res += 1
        return res
            
        