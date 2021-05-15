class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # first rotate the matrix
        box = self.rotate(box)
        # then for each stone, move it all the way down to an obstacle or another stone
        m = len(box)
        n = len(box[0])
        for j in range(n):
            pos = m-1
            for i in range(m-1, -1, -1):
                if box[i][j] == '.':
                    continue
                if box[i][j] == '*':
                    pos = i-1
                    continue
                # if stone, move to pos
                if box[pos][j] == '.':
                    box[pos][j] = '#'
                    box[i][j] = '.'
                pos -= 1
        return box
        
        
    def rotate(self, box):
        m = len(box)
        n = len(box[0])
        res = [['.' for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                res[j][m-1-i] = box[i][j]
        return res
        
