class Solution {
    int[][] Z = {
        {-1,-1}, {-1, 0}, {-1, 1},
        {0, -1}, {0, 1},
        {1, -1}, {1, 0}, {1, 1},
    };
    public void gameOfLife(int[][] board) {
        // four states for each cell:
        // 0->1, 1->0, 1->1, 0->0
        // denote 0->1: 2, 1->0: 3
        int m = board.length;
        int n = board[0].length;
        // first update
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                updateCellFirstStep(board, i, j);
            }
        }
        
        // second update
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                updateCellSecondStep(board, i, j);
            }
        }
    }
    
    public int NumberOfLiveNeighbors(int[][] board, int i, int j) {
        int m = board.length;
        int n = board[0].length;
        int res = 0;
        for (int[] z : this.Z) {
            int x = i+z[0];
            int y = j+z[1];
            if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] % 2 == 1) {
                res++;
            }
        }
        return res;
    }
    
    public void updateCellFirstStep(int[][] board, int i, int j) {
        int nLive = NumberOfLiveNeighbors(board, i, j);
        if (board[i][j] == 1) {
            if (nLive < 2 || nLive > 3) {
                board[i][j] = 3;
            }
        } else {
            if (nLive == 3) {
                board[i][j] = 2;
            }
        }
    }
    
    public void updateCellSecondStep(int[][] board, int i, int j) {
        if (board[i][j] == 2) {
            board[i][j] = 1;
        } else if (board[i][j] == 3) {
            board[i][j] = 0;
        }
        return;
    }
}

