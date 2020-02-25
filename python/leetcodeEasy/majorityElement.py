nums = [3,2,3]
n = len(nums)/2
numDict = dict()
for i in range(len(nums)):
    if nums[i] not in numDict:
        numDict[nums[i]] = 1
    else:
        numDict[nums[i]] = numDict[nums[i]] + 1
print(numDict)
for key in numDict:
    if numDict[key] > n:
        print(key)