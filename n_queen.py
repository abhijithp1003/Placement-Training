def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def safe(board, row, col, n):
    # check verticaly
    for i in range(row):
        if board[i][col] == "Q":
            return False
    # check upper left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # check upper right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True

def solve(board, row, n):
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = "Q"
            solve(board, row+1, n)
            board[row][col] = "."

n = 4
board = [["." for i in range(n)] for i in range(n)]
solve(board, 0, n)



