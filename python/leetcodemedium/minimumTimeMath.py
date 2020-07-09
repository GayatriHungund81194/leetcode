steps=0
points = [[1,1],[3,4],[-1,0]]
for i in range(0,len(points)-1):
    point1 = points[i]
    point2 = points[i+1]
    x = point2[0]-point1[0]
    y = point2[1]-point1[1]
    if abs(x) > abs(y):
        steps = steps+ abs(x)
    elif abs(y) > abs(x):
        steps = steps + abs(y)
    else:
        steps = steps + abs(x)