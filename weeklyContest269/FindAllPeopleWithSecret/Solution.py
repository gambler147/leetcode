class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        shared = set([0, firstPerson])
        
        # merge meetings for same time
        meetings = sorted(meetings, key=lambda x: x[2])
        flag = False
        
        start = set()
        links = collections.defaultdict(list)
        for i, (x,y,t) in enumerate(meetings):
            if i > 0 and t!=meetings[i-1][2]:
                self.dfs(start, links, shared)
                # reset start and links
                start = set()
                links = collections.defaultdict(list)
            if x in shared:
                start.add(x)
            if y in shared:
                start.add(y)
            links[x].append(y)
            links[y].append(x)

        self.dfs(start, links, shared)
        return list(shared)
    
    
    def dfs(self, start,links, shared):
        visited = set()
        while len(start):
            v = start.pop()
            # add v to visited and shared
            visited.add(v)
            shared.add(v)
            # iterate v's neighbors
            for c in links[v]:
                if c not in visited:
                    start.add(c)
