class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        # sliding window, record number of posible window 
        n = len(boxes)
        
        diff = [0 for _ in range(n)] # diff[i] = 1 means ith box is to same port as i+1th box
        for i in range(n-1):
            if boxes[i][0] != boxes[i+1][0]: diff[i] = 1
                
        dp = [0 for _ in range(n)] # dp[i] is the minimum trips to deliver 0-i boxes
        cur = 0 # current weight on the ship
        cbox = 0 # number of different consecutive boxes
        start = 0 # starting index of boxes on current ship
        
        for i in range(n):
            if i - start == maxBoxes:
                cur -= boxes[start][1]
                cbox -= diff[start]
                start+=1
                
            # add box i to current ship
            cur += boxes[i][1]
            if i>0: cbox += diff[i-1]
            
            # drop boxes if weights are too high
            while (cur > maxWeight):
                cur -= boxes[start][1]
                cbox -= diff[start]
                start += 1
            
            # drop boxes if there is no point carrying them, 
            # when there boxes[start] == boxes[start-1] and dp[start] == dp[start-1]
            while start < i and dp[start] == dp[start-1]:
                cur -= boxes[start][1]
                cbox -= diff[start]
                start += 1
            
            dp[i] = dp[start-1] + cbox+2

        return dp[-1]
            
        
        
            
            