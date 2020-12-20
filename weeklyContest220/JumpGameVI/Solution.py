class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # max-heap
        h = []
        n = len(nums)
        for i in range(n):
            while h and h[0][1] < i - k:
                heapq.heappop(h)
            score, j = h[0] if h else (0, -1)
            score *= -1
            cur = score + nums[i]
            heapq.heappush(h, (-cur, i))
            
        for score, i in h:
            if i == n-1:
                return -score
        