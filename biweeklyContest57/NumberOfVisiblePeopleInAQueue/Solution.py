class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # monotonous queue O(n)
        queue = []
        res = []
        for h in heights[::-1]:
            cur = 0
            while queue and queue[-1] < h:
                queue.pop()
                cur += 1
            res.append(cur + int(len(queue) > 0))
            queue.append(h)
        return res[::-1]
    
