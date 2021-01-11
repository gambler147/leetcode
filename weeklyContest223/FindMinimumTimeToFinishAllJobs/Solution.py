class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # we use dfs to go through every job i in list, and assign ith
        # job to any of the k workers. To optimize our efficiency, if we 
        # have found a solution, in later dfs, we do not need to proceed 
        # once the workload for any worker is greater than best result so
        # far. We can use a binary search to shrink our upper bound
        
        def dfs(i, workload, bound):
            # starting from job i, if i==n then we have gone througn all the jobs
            # for given bound, so we return True
            if i == n: return True
            for w in range(k):
                if workload[w] + jobs[i] <= bound:
                    workload[w] += jobs[i]
                    if dfs(i+1, workload, bound):
                        return True
                    workload[w] -= jobs[i]
                    if workload[w] == 0:
                        # assign the most time consuming job to totally free worker
                        break
            return False
        
        n = len(jobs)
        jobs.sort(reverse=True)
        l, r = max(jobs), sum(jobs)
        while l<r:
            m = (l+r)>>1
            workload = [0 for _ in range(n)]
            if dfs(0, workload, m):
                r = m
            else:
                l = m+1
        return l
        