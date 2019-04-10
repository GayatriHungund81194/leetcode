arr = [9,8,7]
for i in range(0,len(arr)):
    key = arr[i]
    j=i-1
    print("j1111:",j)
    while(j>=0 and key<arr[j]):
        arr[j+1] = arr[j]
        j = j-1
    print("j:",j)
    arr[j+1] = key
print(arr)