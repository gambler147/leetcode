class Solution:
    def smallestNumber(self, num: int) -> int:
        # turn to string. O(log(n))
        if num == 0:
            return 0
        neg = num < 0
        num = str(abs(num))
        l = sorted(num)
        # return l[::-1] if negative
        if neg:
            return -int(''.join(l[::-1]))
        
        # find first element that is non negative
        idx = 0
        for i in range(len(l)):
            if l[i] != "0":
                idx = i
                break
                
        # swap 0 and idx
        l[0], l[idx] = l[idx], l[0]
        return int(''.join(l))
    
