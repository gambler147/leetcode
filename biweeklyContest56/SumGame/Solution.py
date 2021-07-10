class Solution:
    def sumGame(self, num: str) -> bool:
        # alice wants to maximize digits diff while Bob wants to minimize
        lsum, rsum = 0, 0
        lqst, rqst = 0, 0
        n = len(num)
        for i in range(n//2):
            if num[i] == '?':
                lqst += 1
            else:
                lsum += int(num[i])
        
        for i in range(n//2, n):
            if num[i] == '?':
                rqst += 1
            else:
                rsum += int(num[i])
                
                
        # it is only possible that either
        # 1. lsum == rsum and lqst == rqst
        # 2. abs(lqst-rqst) %2 == 0 and (lsum - rsum)(lqst - rqst) < 0 and abs(lsum-rsum) == abs(lqst-rqst)//2 * 9
        
        if lsum == rsum and lqst == rqst:
            return False
        
        if abs(lqst-rqst)%2 == 0 and (lsum-rsum)*(lqst-rqst) < 0 and abs(lqst - rqst)//2 * 9 == abs(lsum-rsum):
            return False
        
        return True
    
