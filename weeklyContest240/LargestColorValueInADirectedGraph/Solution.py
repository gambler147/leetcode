class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        dynamic programming.
        
        record maximum number of occurence from a given node. 
        max_count[i][chr] = (max_count[j][chr] for j in i's children), and then max_count[i][colors[i]] += 1
        
        time complexity: O(m+n), space complexity O(m+n)
        
        """
        self.res = 0
        self.colors = colors
        # first detect cycle
        n = len(colors)
        m = len(edges)
        links = collections.defaultdict(set)
        
        for u,v in edges:
            links[u].add(v)
        
        # detect cycle
        if self.is_cyclic(n, links):
            return -1
        
        # if it does not contain cycle, we can simply traverse the graph
        max_colors = [[0 for _ in range(26)] for _ in range(n)] # starting from each node, maximum number of each color
        
        visited = set()
        for i in range(n):
            self.dfs(i, visited, max_colors, links)
        
        return max(map(max, max_colors))
        

    def dfs(self, i, visited, max_colors, links):
        if i in visited:
            return
        color = ord(self.colors[i]) - ord('a')
        for j in links[i]:
            if j not in visited:
                self.dfs(j, visited, max_colors, links)
            
        for c in range(26):
            for j in links[i]:
                max_colors[i][c] = max(max_colors[i][c], max_colors[j][c])
                
        max_colors[i][color] += 1
        visited.add(i)    
                
        
    def is_cyclic(self, n, links):
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            
            # use stack
            cur = set()
            cur.add(node)
            stack = [(node, iter(links[node]))]
            while stack:
                for v in stack[-1][1]:
                    if v in cur:
                        return True
                    elif v not in visited:
                        visited.add(v)
                        cur.add(v)
                        stack.append((v, iter(links[v])))
                        break
                else:
                    v, it = stack.pop()
                    cur.remove(v)
        return False

    