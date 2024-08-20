def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == -1:
                return r, c

    return None, None  

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False 

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True 
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = -1

    return False

def print_board(puzzle):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - -")

        for c in range(9):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")

            if c == 8:
                print(puzzle[r][c])
            else:
                print(str(puzzle[r][c]) + " ", end="")

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    if solve_sudoku(example_board):
        print("Sudoku solved successfully:")
    else:
        print("No solution exists for this Sudoku.")

    print_board(example_board)
