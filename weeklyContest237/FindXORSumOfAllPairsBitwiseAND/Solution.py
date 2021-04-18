class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor = lambda a,b: a^b
        return functools.reduce(xor, arr1) & functools.reduce(xor, arr2)
    
