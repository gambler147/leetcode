class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        m = collections.defaultdict(set)
        for u, a in logs:
            m[u].add(a)
            
        res = [0 for _ in range(k)]
        for u in m.keys():
            res[len(m[u])-1] += 1
        return res
        