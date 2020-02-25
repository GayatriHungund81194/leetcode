arr = [1,1,0,1,1,1,1,0,1]
consOne = 0
finalCons = consOne
flag = 0
arrFinal = list()
for i in range(len(arr)):
    if arr[i] == 1 and flag == 0:
        flag = 1
        consOne = 1
    elif arr[i] == 1 and flag == 1:
        consOne = consOne + 1
    elif arr[i] == 0:
        if flag == 1:
            flag = 0
        if finalCons < consOne:
            finalCons = consOne
        consOne = 0
if finalCons < consOne:
    finalCons = consOne
print(finalCons)
