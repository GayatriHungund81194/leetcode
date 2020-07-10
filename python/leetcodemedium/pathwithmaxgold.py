class Solution:
    def __init__(self):
        self.gold = 0
    def dfs(self,mat,i,j):
        if i > len(mat) or j > len(mat[0]) or mat[i][j] == -1 or i < 0 or j < 0 or mat[i][j] == 0:
            return
        temp = mat[i][j]
        mat[i][j] = -1
        currentgold = currentgold + temp
        if currentgold > self.gold:
            self.gold = currentgold

        self.dfs(i+1,j,g)
        self.dfs(i,j+1,g)
        self.dfs(i-1,j,g)
        self.dfs(i,j-1,g)

        mat[i][j] = temp
    def calldfs(self,matrix):
        