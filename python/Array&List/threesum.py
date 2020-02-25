nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
finalList = []
while (len(nums)>1):
    numCopy = []
    target = nums.pop()
    #print("Array:",nums)
    numCopy = nums.copy()
    #print("Num Copy",numCopy)
    while(len(numCopy)>1):
        out = numCopy.pop()
        pairArray = []

        for i in range(len(numCopy)):
            if (target+numCopy[i]+out==0 and numCopy[i] not in pairArray):
                pairArray.append(numCopy[i])

        if (len(pairArray)>0):
            pairArray.append(out)
            pairArray.append(target)
            finalList.append(pairArray)

print(finalList)