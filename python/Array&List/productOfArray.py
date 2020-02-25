arr = [1,2,3,4]
arr1 = []
arr2 = []
for i in range(len(arr)):
    if i == 0:
        arr1.append(1)
    else:
        arr1.append(arr[i-1]*arr1[i-1])
arr1 = arr1[::-1]
for i in range(len(arr)):
    if i == 0 :
        arr2.append(1)
    else:
        arr2.append(arr[len(arr)-i]*arr2[i-1])
for i in range(len(arr)):
    arr2[i] = arr2[i]*arr1[i]
arr2 = arr2[::-1]
print(arr2)


