class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        # first find kth smallest wonderful integer
        # then we will compare the digits between the origin and new integers
        # to find number of swaps needed. For comparing the two integers, 
        # we compare digit one by one, if current position (i) is not matched, 
        # we find first digit (j) in the remaining new origin that is matched and swap it
        # to current position, and all digits between i and j will be moved 1 position right
        # we can brute force to find the index (O(n)) and move integers to the right
        # time complexity o(nk + n^2), where n is the length of num
        num = list(num)
        n = len(num)
        
        def find_first(i, v, t):
            """find first index j in t that t[j] == v while j >= i"""
            for j in range(i, len(t)):
                if t[j] == v:
                    return j
            return -1
        
        def get_next_wonderful_integer(s):
            # starting from the end of array and find first index i such that s[i] < s[i+1]
            # then start from n-1 to find first index i < j <= n-1 such s[j] > s[i]
            # swap digit i and j, then reverse s[i+1:n]
            # time complexity: O(n)
            n = len(s)
            for i in range(n-2, -1, -1):
                if s[i] < s[i+1]:
                    break
                    
            for j in range(n-1, -1, -1):
                if s[j] > s[i]:
                    break
            t = s    
            # swap i and j
            tmp = t[i]
            t[i] = t[j]
            t[j] = tmp
            t[i+1:] = t[i+1:][::-1]
            return t
        
        t = [v for v in num]
        for _ in range(k):
            t = get_next_wonderful_integer(t)
            
        res = 0
        # compare num and t
        for i in range(len(num)):
            if t[i] != num[i]:
                j = find_first(i, num[i], t)
                tmp = t[j]
                t[i+1:j+1], t[i] = t[i:j], tmp
                res += j-i
                
        return res

