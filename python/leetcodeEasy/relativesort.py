arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
arr3 = []
arr4 = []
finald = {}
for index in arr2:
    for i in range(len(arr1)):
        if (index == arr1[i]):
            finald.setdefault(index,[]).append(arr1[i])
for key in finald:
    arr3 = arr3 + finald[key]
for arrElem in arr1:
    if arrElem not in finald:
        arr4.append(arrElem)
arr4.sort()
arr3 = arr3 + arr4
print(arr3)