nums1 = [4,1,2]
nums2 = [1,3,4,2]
finalNums = list()
numdict = dict()
flag = 0
for i in range(len(nums1)):
    if nums1[i] not in numdict:
        numdict.setdefault(nums1[i],list())
for elem in nums1:
    for i in range(len(nums2)):
        if elem == nums2[i]:
            numdict[elem].append(nums2[i:])
for key in numdict:
    for elem in numdict[key]:
        for i in range(len(elem)):
            print(elem)
            if (elem[i] > key):
                finalNums.append(elem[i])
                flag = 0
                break
            else:
                flag = 1
        if len(elem)==1 or flag == 1:
            finalNums.append(-1)

print("final:",finalNums)
