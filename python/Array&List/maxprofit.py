arr = [3,2,6,5,0,3]
arr1 = arr[:-1]
arr1.sort()
if arr1[0] == 0:
    min = arr1[1]
else:
    min  = arr1[0]
print(min)
max = 0
index = 0
for i in range(len(arr)):
    if arr[i] == min:
        index = i
        break
arr1 = arr[index:]
arr1.sort(reverse = True)
max = arr1[0]
profit = max - min
print(profit)

