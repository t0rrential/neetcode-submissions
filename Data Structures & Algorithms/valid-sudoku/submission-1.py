class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bl = len(board)

        for i in range(bl):
            for j in range(bl):
                if i%3 ==0 and j%3 == 0:
                    s = [int(board[i + k//3][j + k%3]) for k in range(bl) if board[i+k//3][j+k%3].isdigit()]

                    if len(s) != len(set(s)):
                        return False
                

                r = [int(d) for d in board[i] if d.isdigit()]
                c = [int(board[k][j]) for k in range(bl) if board[k][j].isdigit()]

                rs = set(r)
                cs  = set(c)

                # print(f"{r}\n{c}\n")

                if len(rs) != len(r) or len(cs) != len(c):
                    return False
        return True



