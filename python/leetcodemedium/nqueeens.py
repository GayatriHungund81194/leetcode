global N 
N = 4

#to print the solution
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print(board[i][j]) 
        print("")

#to check if the left side col and diagonal is safe
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i in range(row):
        if board[i][col] == 1:
            return False
    
    








def solveNQ():
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    printSolution(board)

solveNQ()