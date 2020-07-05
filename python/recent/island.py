adjMat = [[1,1,1,1,0],[1,1,1,1,0],[1,1,0,0,0],[0,0,0,0,0]]
def bfs(adjMat,row,col,i,j):
    if adjMat[i][j] == 0:
        return 
    adjMat[i][j] = 0
    

def numislands(adjMat):
    if not adjMat:
        return None
    row = len(adjMat)
    col = len(adjMat[0])

    cnt = 0

    for i in range(row):
        for j in range(col):
            if (adjMat[i][j] == 1):
                bfs(adjMat,row,col,i,j)
                count = count + 1
