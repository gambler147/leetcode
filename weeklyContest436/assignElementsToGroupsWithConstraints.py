class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        import collections
        val_to_ind_map = collections.defaultdict(list)
        for i,e in enumerate(elements):
            val_to_ind_map[e].append(i)

        print(val_to_ind_map)

        res = []
        for g in groups:
            ans = float('inf')
            for v in range(1, int(math.sqrt(g))+1):
                if g%v == 0:
                    if v in val_to_ind_map:
                        ans = min(ans, val_to_ind_map[v][0])
                    if g // v in val_to_ind_map:
                        ans = min(ans, val_to_ind_map[g // v][0])

            res.append(ans if ans != float('inf') else -1)
        return res

