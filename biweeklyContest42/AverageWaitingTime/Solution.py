class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur = 0 # current timestamp
        wait_sum = 0 # total wait time
        for a, t in customers:
            if cur < a:
                # start with customers time
                cur = a
                
            # wait time is cur + t - arrival time
            cur += t
            wait_sum += cur - a
        return wait_sum / len(customers)
    