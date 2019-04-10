arr = [9,8,7,6,5,4,3,2]
for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
        if (arr[min]>arr[j]):
            min=j
    temp = arr[min]
    arr[min]=arr[i]
    arr[i]=temp
print(arr)
