
# my solution O(MN)/O(MN)
from collections import deque, defaultdict
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_fin_idx = len(grid)-1 ## idx이므로 길이에서 1 차감
        col_fin_dix = len(grid[0])-1
        Memo_table = defaultdict(lambda : 0)
        Memo_table[0,0] = grid[0][0]
        Q = deque(Memo_table.keys())
        while Q:
            row, col = Q.popleft()
            if row + 1 <= row_fin_idx:
                if not Memo_table[row + 1, col]:
                    Memo_table[row + 1, col] = Memo_table[row, col] + grid[row + 1][col]
                    Q.append((row + 1, col))
                else:
                    if Memo_table[row, col] + grid[row+1][col] < Memo_table[row + 1, col]:
                        Memo_table[row + 1, col] = Memo_table[row, col] + grid[row+1][col]
            if col + 1 <= col_fin_dix:
                if not Memo_table[row, col + 1]:
                    Memo_table[row, col + 1] = Memo_table[row, col] + grid[row][col + 1]
                    Q.append((row, col + 1))
                else:
                    if Memo_table[row, col] + grid[row][col+1] < Memo_table[row, col + 1]:
                        Memo_table[row, col + 1] = Memo_table[row, col] + grid[row][col + 1]
        return Memo_table[row_fin_idx, col_fin_dix]

#other solution O(MN)/O(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # if m > 1:
        for i in range(1,m):
            grid[i][0] = grid[i][0] + grid[i-1][0]
        # if n > 1:
        for i in range(1,n):
            grid[0][i] = grid[0][i] + grid[0][i-1]
        
        for i in range(1,m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        print(grid)
        return grid[-1][-1]
