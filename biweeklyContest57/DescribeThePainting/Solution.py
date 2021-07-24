class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # sort by start and end points separately. O(nlogn)
        entry = []
        for s, e, color in segments:
            entry.append((s, 1, color))
            entry.append((e, -1, color))
            
        entry.sort()
        
        res = [ ]
        # loop through the endpoints, if there are multiple endpoints of starting and ending points. 
        # handle endpoints first
        i = 0
        cur = 0 # current color
        prev = 0 # current position in number line
        n = len(entry)
        while i < n:
            pos, flag, color = entry[i]
            # append previous to list
            if cur > 0 and pos > prev:
                res.append([prev, pos, cur])
            
            cur += flag*color # add previous color
            while i+1 < n and entry[i+1][0] == pos and entry[i+1][1] == flag:
                cur += flag*entry[i+1][2]
                i += 1
                
            prev = pos
            i += 1
        return res
                
            
