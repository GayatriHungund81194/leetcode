# class Solution:
#     def __init__(self):
#         self.ll = list()

#     def findPairs(self,curr,st):
#         if (st == st[::-1]):
#             self.ll.append(st)
# nums = ababcc
# for count in range(len(nums)):
#     for 
nums = "babad"
ll = list()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        num = nums[i:j+1]
        if (num==num[::-1]):
            ll.append(num)
    print(max(ll,key=len))

