class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        # for all good-bad combinations, check if all statements have no contradictions
        # brute force. O(n^2 * 2**n)
        n = len(statements)
        
        res = 0
        for mark in range(2**n):
            bin_ = bin(mark)[2:].zfill(n)
            
            # check for contradiction
            valid = False
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    
                    if bin_[i] == '1' and statements[i][j] != 2 and bin_[j] != str(statements[i][j]):
                        valid = False
                        break
                    
                    if bin_[j] == '1' and statements[j][i] != 2 and bin_[i] != str(statements[j][i]):
                        valid = False
                        break
                else:
                    continue
                break
            else:
                valid = True
                
            if valid:
                res = max(res, bin_.count('1'))
                
        return res
        
        
        
