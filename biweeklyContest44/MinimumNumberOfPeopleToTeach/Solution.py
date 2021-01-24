class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # first find unmber of friendships that connot communicate
        # then find min of the number of total friends k minus number of friends who can speak language i
        languages = [None] + [set(l) for l in languages]
        
        non_comm = collections.Counter()
        for f, g in friendships:
            if len(languages[f].intersection(languages[g])) == 0:
                non_comm[f] += 1
                non_comm[g] += 1
        # iterate all possible languages    
        res = len(non_comm)
        for i in range(1, n+1):
            cur = 0
            for f in non_comm:
                if i not in languages[f]:
                    cur += 1
            res = min(res, cur)
        return res
    
