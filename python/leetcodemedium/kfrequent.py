import operator
nums = [3,0,1,0]
k = 2
count = 1
numdict = dict()
freqnums = list()
for i in range(len(nums)):
    if nums[i] not in numdict:
        numdict[nums[i]] = 1
    else:
        numdict[nums[i]] = numdict[nums[i]] + 1
sorted_numdict = sorted(numdict.items(), key=operator.itemgetter(1))
for key in numdict:
    if count <= k:
        freqnums.append(key)
    count = count + 1
print(freqnums)
print(numdict)


