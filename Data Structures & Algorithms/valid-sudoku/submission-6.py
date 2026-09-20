class Solution():

    def __init__(self):
        self.int_dict = {}
        self.reset_int_dict()
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        board==[[".",".",".",".","5",".",".","1","."],
                [".","4",".","3",".",".",".",".","."],
                [".",".",".",".",".","3",".",".","1"],
                ["8",".",".",".",".",".",".","2","."],
                [".",".","2",".","7",".",".",".","."],
                [".","1","5",".",".",".",".",".","."],
                [".",".",".",".",".","2",".",".","."],
                [".","2",".","9",".",".",".",".","."],
                [".",".","4",".",".",".",".",".","."]]
            
        if (self.check_all_rows(board) and 
            self.check_all_columns(board) and
            self.check_all_mats(board)):
            return True
        else:
            return False

    def check_all_rows(self,board):
        for l in board:
            if not self.check_list(l):
                return False
        return True
    
    def check_all_columns(self,board):
        for i in range(0,len(board)):
            col = [l[i] for l in board]
            if not self.check_list(col):
                return False
        return True

    def check_all_mats(self,board):
        mat = []
        for m in [0,3,6]:
            for k in [0,3,6]:
                mat = []
                for i in [m + 0,m + 1,m + 2]:
                    for j in [k + 0,k + 1,k + 2]:
                        mat.append(board[i][j])
                    if not self.check_list(mat):
                        return False
        return True
        

    def check_list(self, l):
        self.reset_int_dict()
        for i, n in enumerate(l):
            if n == ".":
                continue
            if self.int_dict[n] == True:
                return False
            else:
                self.int_dict[n] = True
        self.reset_int_dict()
        return True
    
    def reset_int_dict(self):
        self.int_dict = {
            '1': False,
            '2': False,
            '3': False,
            '4': False,
            '5': False,
            '6': False,
            '7': False,
            '8': False,
            '9': False,
        }
    
            