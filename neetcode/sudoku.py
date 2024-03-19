from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isUnique(row):
                return False
    
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isUnique(column):
                return False

        for row in range(0,9,3):
            for col in range(0, 9, 3):
                box = [board[r][c] for r in range(row, row+3) for c in range(col, col+3)]
                if not self.isUnique(box):
                    return False

        return True
        
    def isUnique(self, items:List[str]) -> bool:
        elements = [item for item in items if item != '.']
        return len(elements) == len(set(elements))

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))