nums = [1,1,2,1,1]
k = 3
from collections import defaultdict
total = 0
count = 0
for i in range(len(nums)):
    if(nums[i]%2==0):
        nums[i] = 0
    else:
        nums[i] = 1
trackTotal = defaultdict(lambda: 0)
print(trackTotal)
for i in range(len(nums)):
    total+=nums[i]
    if(total == k):
        count+=1
    if(total - k in trackTotal):
        count+=trackTotal[total-k]
    trackTotal[total] += 1
print(count)