nums = [1, 5, 1, 1, 6, 4]

tmp = list(nums)
tmp.sort(reverse = True)
print(tmp)
mid = len(nums) // 2 
j = 1
for i in range(mid):
    nums[j] = tmp[i]
    j += 2
    print(nums)
j = 0
for i in range(mid, len(nums)):
    nums[j] = tmp[i]
    j += 2
    print(nums)