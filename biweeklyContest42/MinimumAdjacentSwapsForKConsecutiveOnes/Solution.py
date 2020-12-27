class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # we use a rolling window, which keeps indices of consecutive k appearences of 1s
        # lets say the index of 1s in current window is A = [a0, a1, ... ak-1]
        # then we are trying to find an index x, such that
        # we transform A to consecutive indices [x, x+1, ... x+k-1].
        # Notice the moves needed is |a0 - x| + |a1 - (x+1)| + ... + |a(k-1) - (x+k-1)|
        # do a little transformation -> |a0-x| + |(a1-1) - x| + |(a(k-1) - (k-1)) - x|
        # it is obvious that when x is the median of [a0, a1-1, a2-2, ... a(k-1) - (k-1)]
        # the solution reach the minimum
        # Also, notice that if we shift A for any constant, that is for each i, ai -> ai+a,
        # the median x changes but the summation does not change
        # therefore, for ith occurence of 1, we subtract its index with k, ai -> ai-i.
        
        # To find the rolling maximum value of c = |a0-x| + |(a1-1) - x| + |(a(k-1) - (k-1)) - x|
        # we just need to update the value instead of recalculating. 
        # When we update the median from x -> y, for the first
        # half A we add (y-x) to each of them, for the second half of A we subtract (y-x)
        # and we need to remove |a0-x| and include |ak-y| where ak is the next index of 1
        
        ones = []
        for i in range(len(nums)):
            if nums[i] == 1:
                ones.append(i - len(ones))
                
        # rolling window
        cur = 0
        # calculate initial summation
        med = k//2
        for i in range(k):
            cur += abs(ones[i] - ones[med])
            
        res = cur
        # rolling window update 
        for i in range(1, len(ones) - k + 1):
            # find median of ones[i:i+k]
            new_med = k//2+i
            if k%2==0:
                # if k is odd, the sum of abs difference will not change excluding the first value
                cur += ones[new_med] - ones[med] 
            # update first value and last value
            cur -= ones[med] - ones[i-1]
            cur += ones[i+k-1] - ones[new_med]
            med = new_med
            res = min(res, cur)
        return res
        
        