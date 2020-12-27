class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # you bubble up next 0 to pair with the previous 0
        # so if there are total k 0s, you have to pair all 
        # 0s from i to i + k - 1, let i be the index of first 0s
        n = len(binary)
        k = 0
        idx = -1
        for i, b in enumerate(binary):
            if b == '0':
                k += 1
                if idx == -1:
                    idx = i         
        # index of 0 for the final string is at position idx + k - 1
        res = '1' * (idx + k - 1) + '0' + '1' * (n - idx - k) if idx != -1 else binary
        return res
        
        