# arr = [-2,1]
# arr1 = []
# arr2 = []
# count = 0
# maxSum = -99999
# add = 0
# for i in range (len(arr)):
#     arr2 = arr[i:]
#     while count!=len(arr2)-1:
#         arr1.append(arr2[count])
#         print("Initial array:",arr1)
#         for j in range(len(arr1)):
#             add = add + arr1[j]
#         print("Addition:",add)
#         if maxSum < add:
#             maxSum = add
#         add = 0
#         count = count + 1
#     count = 0
#     arr1.clear()
# print(maxSum)

# i=len(nums)

nums=[1,2,3,4,5,6]
i=len(nums)
# my_sum= what is the sum that i am seeing currently
# overall sum= what is the sum that i am seeing globally

my_sum=nums[0]
overall_sum=nums[0]
for i in range(1,len(nums)):
    my_sum=max(nums[i],my_sum+nums[i])
    overall_sum = max(my_sum,overall_sum)














