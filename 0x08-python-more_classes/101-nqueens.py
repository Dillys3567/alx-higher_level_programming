#!/usr/bin/python3
"""Solve the nqueens puzzle.

Args:
    board (list): list represnting chessboard
    solutions (list): list of solutions

queen must be on chessboardd
"""
import sys

def init_board(n):
    """Initialize chessboard"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)

def board_deepcopy(board):
    """return copy of board"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)

def get_solution(board):
    """Return list of solved chessboard
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)

def xout(board, row, col):
    """X out spots on a chessboard.

    Args:
    board (list): current chessboard.
    row (int): row where queen was
    col (int): column where queen was
    """
    #forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    #backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    #spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    #spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    #spots diagonal right down
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    #spots diagonal up left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    #spots diagonal right up
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    #spots diagonal to left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -=1

def recursive_solve(board, row, queens, solutions):
    """Recursive;y solve puzzle
    Args:
        board (list): current chessboard
        row (int): current working row
        queens (int): current number of queens
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)
    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)
    return (solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)


