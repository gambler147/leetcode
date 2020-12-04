class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if self.helper(p1,p2,p3,p4): return True
        if self.helper(p1,p3,p2,p4): return True
        if self.helper(p1,p3,p4,p2): return True
        return False
        
    def helper(self, p1, p2, p3, p4):
        def norm2(v):
            return v[0]**2 + v[1]**2
    
        def prod(v1, v2):
            return v1[0]*v2[0] + v1[1]*v2[1]
        
        v1 = [p2[0] - p1[0], p2[1] - p1[1]]
        v2 = [p3[0] - p2[0], p3[1] - p2[1]]
        v3 = [p4[0] - p3[0], p4[1] - p3[1]]
        v4 = [p1[0] - p4[0], p1[1] - p4[1]]
        
        if norm2(v1) != 0 and (norm2(v1) == norm2(v2) == norm2(v3) == norm2(v4)) and (prod(v1,v2) == prod(v2,v3) == prod(v3,v4) == prod(v4,v1) == 0):
            return True
        return False
