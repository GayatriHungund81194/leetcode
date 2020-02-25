arr = [1,8,6,2,5,4,8,3,7]
left  = 0
right = len(arr)-1
maxDist = len(arr)-1
maxArea = 0
area = 0
for i in range(len(arr)):
    height = min(arr[left],arr[right])
    length = maxDist
    area  = length * height
    if area > maxArea:
        maxArea = area
    if (arr[left] < arr[right]):
        left = left + 1
        maxDist = maxDist - 1
    else:
        right = right -1
        maxDist  = maxDist - 1
