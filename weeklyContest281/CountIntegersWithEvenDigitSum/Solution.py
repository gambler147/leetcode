class Solution:
    def countEven(self, num: int) -> int:
        cur = 0
        for v in str(num):
            cur += int(v)
        return (num - int(cur%2!=0))//2
    
