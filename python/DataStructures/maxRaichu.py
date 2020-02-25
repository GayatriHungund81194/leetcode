
nums=[-2,3,-4]
i=len(nums)
# my_sum= what is the sum that i am seeing currently
# overall sum= what is the sum that i am seeing globally

my_sum=nums[0]
overall_sum=nums[0]
for i in range(1,len(nums)):
    my_sum=max(nums[i],my_sum*nums[i])
    overall_sum = max(my_sum,overall_sum)
print(overall_sum)