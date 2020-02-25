numbers = [2,7,11,15]
target = 9
indList = list()
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if (numbers[i]+numbers[j] == target):
            indList.append(i+1)
            indList.append(j+1)
print(indList)
