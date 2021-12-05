class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # O(n^3) permutations
        from itertools import permutations
        n = len(digits)
        s = set()
        for a,b,c in permutations(digits, 3):
            if a != 0 and c%2 == 0:a
                s.add(100*a+10*b+c)
        return sorted(s)
