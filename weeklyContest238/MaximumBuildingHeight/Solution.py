class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        """
        We first sort restrictions by the height. We start from the index with smallest restriction,
        the height of building at this index is completely determined by the exact established building
        to the left of current index and to the right of current index and the height restriction itself.
        
        Let's say the current index is i, with height restriction h and left and right (if there is) existing buildings 
        with index l and r, height hl and hr, respectively. Then the maximum height for building i 
        can be 
            min(hl + i - l, hr + r - i, h)
            
        So we use a sorted list to record indices of established buildings and in each iteration we use
        binary search to find current building's left and right buildings.
        
        Total time complexity is O(nlogn), (sorting; loop with sorted list), space is O(n)
        """
        from sortedcontainers import SortedList
        
        # initialization
        built_idx = SortedList()  # indices in which buildings have been placed
        built_idx.add(1)
        height = {1: 0}
        # sort restrictions by the height
        restrictions.sort(key = lambda x: x[1]) 
        
        for idx, h in restrictions:
            # find idx's previous and next indices using binary search
            key = built_idx.bisect_left(idx)
            prev = built_idx[key-1]
            # current building's height cannot exceed prev building's height + distance between them
            height[idx] = min(height[prev] + (idx-prev), h)
            if key < len(built_idx):
                # if there is a building after current one, this building's height is also restricted
                nxt = built_idx[key]
                height[idx] = min(height[idx], height[nxt] + (nxt-idx))
            # add this index to the sorted list
            built_idx.add(idx)
            
        """
        some of the buildings are not placed yet since their heights are not restricted
        we now iterate each pair of consecutive established buildings, determine maximum height of building
        that can be placed between them.
        Let's say if two buildings with indices l and r, with heights hl and hr. 
        Let's assume hl <= hr (easy to prove the other way around)
        then we can prove the maximum height between this two buildings is
        
        hr + (hl + (r-l) - hr) // 2
        or
        hl + (hr + (r-l) - hl) // 2   (if hl > hr)
        """
        
        height = sorted(height.items())
        res = 0
        for i in range(len(height)-1):
            l, hl = height[i]
            r, hr = height[i+1]
            # print(l, r, hl, hr)
            res = max(res, hl, hr, max(hl, hr) + (min(hl,hr) - max(hl,hr) + (r-l))//2) 
            
        # if the last index of established building is not n, we build buildings after this index until n
        if height[-1][0] != n:
            r, hr = height[-1]
            res = max(res, hr + n-r)
        return res
        