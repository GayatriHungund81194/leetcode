n = 5
arr = list()
i=0
j=1
for k in range(5):
    if k == 0:
        arr.append(k)
    if k == 1:
        arr.append(k)
    if k > 1:
        s=arr[i]+arr[j]
        arr.append(s)
        i = i+1
        j = j+1
print(arr)