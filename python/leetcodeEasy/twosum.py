class Solution:
    
    def __init(self,nums,target):
       
        sum=0
        nums=list()
        target=0

    def twoSum(self, nums, target):
        #num = sorted(nums)
        print("",nums)
        count=1
        sum=0
        retlist = list()

        for x in range(len(nums)):
            for y in range(1,len(nums)):
                if x!=y:
                    sum = nums[x]+nums[y]
                    if sum == target:
                        retlist.append(x)
                        retlist.append(y)
                        return retlist
sol  = Solution()
nums = [2,5,5,11]
l = sol.twoSum(nums,10)
print("",l)