class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # count edges for each node, and for each node, find number of nodes that they together
        # have more than queries[i] incidents using binary search. 
        # We need to subtract the edges between them by looping through the edges, which is 10**5. 
        # The overall time complexity is O(q * (nlogn + E))
        freq = collections.Counter()
        edge_freq = collections.Counter()
        
        for u,v in edges:
            freq[u] += 1
            freq[v] += 1
            edge_freq[(min(u,v), max(u,v))] += 1
        
        # sort freq for further binary search
        freq_sorted = sorted(freq.values())
        # add nodes that do not have edges
        freq_sorted = [0] * (n - len(freq_sorted)) + freq_sorted
        
        res = []
        # loop through queries
        for q in queries:
            # loop through each value in freq_sorted[i], 
            # find number of elements whose value is greater than q - freq_sorted[i]
            cur = sum(n - bisect.bisect_right(freq_sorted, q - freq_sorted[i]) for i in range(n))
            # subtract diagonal cases
            cur -= n - bisect.bisect_right(freq_sorted, q//2)
            cur //= 2
            
            # loop through edges check if each pair is still valid by subtracting internal edges
            for u,v in edge_freq:
                if freq[u] + freq[v] > q and freq[u] + freq[v] - edge_freq[(u,v)] <= q:
                    cur -= 1
            res.append(cur)
            
        return res
    