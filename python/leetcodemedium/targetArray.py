nums = [0,1,2,3,4]
index = [0,1,2,2,1]
l=[]
for i in range(len(nums)):
    l.insert(index[i],nums[i])
print(l)