grid = [[0,6,0],[5,8,7],[0,9,0]]
rows = len(grid)
cols = len(grid[0])
def dfs(i,j):
    if i< 0 or i > rows-1 or j < 0 or j > cols-1 or grid[i][j] == 0 or grid[i][j] == -1:
        return
    tmp  =  grid[i][j]
    grid[i][j] = -1
    print(grid)

    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j-1)
    dfs(i,j+1)

    grid[i][j] = tmp
    print("After temp:",grid)

for i in range(rows):
    for j in range(cols):
        if grid[i][j] != 0:
            dfs(i,j)