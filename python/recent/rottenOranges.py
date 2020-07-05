grid = [[2,1,0,2,1],[1,0,1,2,1],[1,0,0,2,1]]
rotten = list()
r = len(grid)
c = len(grid[0])
count = 0
count2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 2:
            rotten.append((i,j))
        if grid[i][j] == 1:
            count = count + 1
while rotten:
    for k in range(len(rotten)):
        print("Rotten:",rotten)
        i,j = rotten.pop(0)
        for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if (0<=x<r and 0<=y<c and grid[x][y]==1):
                grid[i][j] = 2
                count = count - 1
                rotten.append((x,y))
    count2 = count2 + 1
if cnt == 0:
    print(max(0, res-1))
else:
    print("-1")