def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    horizontal_line = "+-------+-------+-------+"

    for i in range(9):
        if i % 3 == 0:
            print(horizontal_line)
        row_str = "|"
        for j in range(9):
            if j % 3 == 0:
                row_str += " "
            if board[i][j] == 0:
                row_str += " "
            else:
                row_str += str(board[i][j])
            row_str += " "
            if j == 8:
                row_str += "|"
            elif (j + 1) % 3 == 0:
                row_str += "|"
        print(row_str)
        

    print(horizontal_line)

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]


if solve_sudoku(grid):
    print("Brawo, rozwiązałeś sudoku:")
    print_board(grid)
