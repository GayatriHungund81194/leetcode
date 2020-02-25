arr = [34,23,11,24,75,33,54,18]
arr1 = sorted(arr)
print(arr1)
minArr = list(str(arr1[0]))
print(minArr)
for i in range(len(minArr)):
    minArr[i] = int(minArr[i])
print(minArr)
sum = 0
for i in range(len(minArr)):
    sum = sum + minArr[i]
print(sum)
