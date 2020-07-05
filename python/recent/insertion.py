arr = [1,6,4,5]
elem = 3

for i in range(1,len(arr)):
    value = arr[i]
    j = i - 1
    while(j >=0):
        if value < arr[j]:
            print("i",i)
            print("j",j)
            arr[j+1] = arr[j]
            arr[j] = value
            j = j - 1
        else: 
            break
print(arr)