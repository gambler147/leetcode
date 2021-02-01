class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # brute force O(nlogn)
        counter = collections.Counter()
        for k in range(lowLimit, highLimit+1):
            s = 0
            while k:
                s += k%10
                k //= 10
            counter[s] += 1
        return max(counter.values())
    