nums = [1,2,3,4,3]
flag = 0
li = list()
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if i!=j and nums[j]>nums[i]:
            li.append(nums[j])
            flag = 1
            break
    if flag==0:
        for m in range(0,i):
            if i!=m and nums[m]>nums[i]:
                li.append(nums[m])
                flag = 1
                break
    if flag!=1:
        li.append(-1)
    flag = 0
print(li)



