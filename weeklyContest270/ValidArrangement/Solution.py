class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Eulerian path. O(n)
        n = len(pairs)
        din, dout = collections.Counter(), collections.Counter()
        graph = collections.defaultdict(list)
        for i,(s, e) in enumerate(pairs):
            din[e] += 1
            dout[s] += 1
            graph[s].append(e)
            
        start = pairs[0][0]
        # determine start node, if a node has 1 more degree in out than in in, it has to be start node
        for v in dout:
            if dout[v] - din[v] == 1:
                start = v
                break
            
        res = []
        stack = [start]
        # Hierholzer's algorithm
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())
        
        return [[res[i+1], res[i]] for i in range(len(res)-2, -1, -1)]
