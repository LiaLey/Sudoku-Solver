from copy import deepcopy

class Sudoku():
    def __init__(self, board=None):
        empty_board = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ]
        self.default = board or empty_board
        self.board = board or empty_board

    def put(self, row, col, number):
        if not (number > 0 and number <= 9):
            raise ValueError("Number must be between 0 and 9!")
        if default[row][col] == 0:
            board[row][col] == number

    def get_cell_to_fill(board):
        for r, row in enumerate(board):
            for c, item in enumerate(row):
                if item == 0:
                    return (r, c)

    def valid_answers(board):
        def which_square(r, c):
            my_map = {0:1, 1:1, 2:1, 3:4, 4:4, 5:4, 6:7, 7:7, 8:7}
            return (my_map[r], my_map[c])
        def check_h(row):
            return {1,2,3,4,5,6,7,8,9}.difference(set(row))
        def check_v(col):
            return {1,2,3,4,5,6,7,8,9}.difference(set(col))
        def check_square(square):
            return {1,2,3,4,5,6,7,8,9}.difference(set(square))
        x, y = Sudoku.get_cell_to_fill(board)
        my_row = board[x]
        my_col = []
        my_square = []
        for row in board:
            my_col.append(row[y])
        sx , sy = which_square(x, y)
        my_square.append(board[sx-1][sy-1])
        my_square.append(board[sx-1][sy])
        my_square.append(board[sx-1][sy+1])
        my_square.append(board[sx][sy-1])
        my_square.append(board[sx][sy])
        my_square.append(board[sx][sy+1])
        my_square.append(board[sx+1][sy-1])
        my_square.append(board[sx+1][sy])
        my_square.append(board[sx+1][sy+1])
        ans = check_h(my_row).intersection(check_v(my_col).intersection(check_square(my_square)))
        res = []
        for n in ans:
            temp_board = deepcopy(board)
            temp_board[x][y] = n
            res.append(temp_board)
        return res

    def solve(part):
        def completed(part):
            return Sudoku.get_cell_to_fill(part) == None

        if completed(part):
            return part
        else:
            res = []
            for o in Sudoku.valid_answers(part):
                res += Sudoku.solve(o)
            return res

    def __str__(self):
        Game.print_board(self.board)
        return ""

class Game():
    def __init__(self, empty=True):
        if empty:
            self.sudoku = Sudoku()
        else:
            board = None
            while True:
                try:
                    my_string = input("Enter board in String format: ")
                    board = Game.read_string(my_string)
                    break
                except ValueError:
                    pass
                except :
                    print("Unexpected Error!")
            self.sudoku = Sudoku(board)

    def play(self):
        pass

    def read_string(string):
        if len(string) != 81:
            raise ValueError("Not enough arguments!")
        board = []
        temp = []
        for char in string:
            if not (int(char) >= 0):
                raise ValueError("Argument must be between 0 and 9!")
            if len(temp) < 9:
                temp.append(int(char))
            else:
                board.append(temp)
                temp = []
                temp.append(int(char))
        board.append(temp)
        return board

    def print_board(board):
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                n = item
                if item == 0:
                    n = ' '
                if j % 3 == 0:
                    print(f"|{n: ^3}", end='')
                else:
                    print(f"{n: ^3}", end='')
                if j == 8:
                    print("|")

            if (i+1) % 3 == 0:
                print("  -  -  -   -  -  -   -  -  -")

board = Game.read_string("400000000000009000000000785007048050001300000006070000860000903700005062003700000")
s = Sudoku(board)
Game.print_board(Sudoku.solve(s.board))



def postorder(self):
    self.postorder_aux(1)

def postorder_aux(self, k):
    if k <= self.count:
        postorder_aux(2*k)
        postorder_aux(2*k+1)
        print(self.array[k])