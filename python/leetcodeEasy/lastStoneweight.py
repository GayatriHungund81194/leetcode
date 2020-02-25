arr = [2,7,4,1,8,1]
arr1 = sorted(arr)
while len(arr1) > 1:
    arr1 = sorted(arr1)
    arr1 = arr1[::-1]
    arr1[0] = arr1[0] - arr1[1]
    arr1.remove(arr1[1])
print(arr1)


