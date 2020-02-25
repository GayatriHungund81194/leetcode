nums = [0,1,0,3,12]
j = 0
countZero = 0
for i in range(len(nums)):
    if nums[i] == 0:
        countZero = countZero+1
    else:
        nums[j] = nums[i]
        j = j + 1
print(nums)