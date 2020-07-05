cells = [0,1,0,1,1,0,0,1]

N = 7

while N > 0:
    updated = [0]*8
    print("N",N)
    for i in range(1,len(cells)-1):
        if ((cells[i-1]==0 and cells[i+1]==0) or (cells[i-1]==1 and cells[i+1]==1)):
            updated[i] = 1
    print("Day:",updated)
    cells = updated
    print("cells",cells)
    N = N - 1