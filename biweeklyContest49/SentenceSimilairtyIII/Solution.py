class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        l1,l2 = s1.split(), s2.split()
        n1,n2 = len(l1), len(l2)
        if n2 < n1:
            # switch if s2 is shorter
            l1,l2,n1,n2 = l2,l1,n2,n1

        # two pointer for array 2
        i, j = 0, n1-1
        # left
        while i < n1:
            if l1[i] == l2[i]:
                i+=1
            else:
                break
        
        # right
        while j >= 0:
            if l1[j] == l2[j + (n2-n1)]:
                j-=1
            else:
                break
        
        return j < i
