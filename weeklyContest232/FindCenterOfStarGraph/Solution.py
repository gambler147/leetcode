class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # simply find which node has the most edge
        # O(E) == O(n) time complexity, O(1) space
        n = len(edges)+1
        s = sum(sum(e) for e in edges)
            
        # note: s == n(n+1)/2 + c*(n-2)
        return (s - n*(n+1)//2) // (n-2)
        