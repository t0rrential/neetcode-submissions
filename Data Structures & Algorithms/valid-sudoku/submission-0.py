class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9

        for i in range(0, 9):
            print(board[i])

        for i in range(0, length):
            row = list(filter(lambda x: x != ".", board[i]))

            if len(set(row)) != len(row):
                print(f"row: {row}")
                return False

            col = [board[j][i] for j in range(0, length)] 
            col = list(filter(lambda x: x != ".", col))

            if len(set(col)) != len(col):
                print(f"col: {col}")
                return False

            square = []

            for r in range((i//3)*3, (i//3)*3+3):
                for c in range((i%3)*3, (i%3)*3+3):
                    if board[r][c] != ".":
                        square.append(board[r][c])
                            
            print(square)

            if len(set(square)) != len(square):
                return False
        return True