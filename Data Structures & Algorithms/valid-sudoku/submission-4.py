class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        square = defaultdict(list)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                value = board[row][col]
                if (value in rows[row]
                 or value in cols[col]
                 or value in square[(row // 3, col // 3)]):
                    return False
                rows[row].append(value)
                cols[col].append(value)
                square[(row // 3, col // 3)].append(value)
        return True

                