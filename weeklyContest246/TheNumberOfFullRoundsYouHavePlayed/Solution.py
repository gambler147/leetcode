class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        sh, sm = list(map(int, startTime.split(':')))
        fh, fm = list(map(int, finishTime.split(':')))
        
        # if finish time is less than start time, we add 24 hours
        if fh < sh or (fh == sh and fm < sm):
            fh += 24
        # make starting time to the next 15-min time
        if sm%15 != 0:
            sm = sm + (15 - sm%15)
            if sm == 60:
                sh += 1
                sm = 0
        # make finish time to the previous 15-min time
        if fm%15 != 0:
            fm = fm - fm%15
        
        mins = (fh - sh) * 60 + (fm - sm)
        return mins//15
    
        