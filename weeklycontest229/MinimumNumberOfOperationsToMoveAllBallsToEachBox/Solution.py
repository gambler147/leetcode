class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # use lc and rc to record number of balls on the left or right side of ith boxes
        # and record operations needed for left balls lm and right balls rm
        lc, rc = 0, 0 # left count , right count
        lm, rm = 0, 0 # left moves, right moves
        n = len(boxes)
        # initialize
        for i in range(1, n):
            rc += int(boxes[i])
            rm += int(boxes[i]) * i # moves needed from box i to box 0
            
        res = [0 for _ in range(n)]
        
        for i in range(n):
            # update result = moves from left + moves from right
            res[i] = lm + rm 
            # update lc, rc, lm, rm
            tmp = int(boxes[i])
            lm += lc + tmp
            rm -= rc 
            lc += tmp
            rc -= int(boxes[i+1]) if i+1 < n else 0

        
        return res
    