class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # O(26n)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
            
        # greedy
        res = []
        repeat = 0 # repeat times
        while True:
            for i in range(25, -1, -1):
                # append this character if count is greater than 0 and not appear 3 times before
                if count[i] > 0:
                    if res and res[-1] == i:
                        if repeat < repeatLimit:
                            repeat += 1
                            res.append(i)
                            count[i] -= 1
                        else:
                            continue
                    else:
                        repeat = 1
                        res.append(i)
                        count[i] -= 1
                    break
            else:
                # no available characters
                break
                
        return ''.join([chr(i + ord('a')) for i in res])
    
