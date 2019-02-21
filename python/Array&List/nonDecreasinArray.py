class Solution:
    def checkPossibility(self, nums: 'List[int]') -> 'bool':
        count =0
        x=0
        diff = 0
        flag= False
        print("",len(nums))
        for x in range(len(nums)):
            print("Count",x)
            if x+1 < len(nums):
                if nums[x]>nums[x+1] and  nums[x+1]-nums[x]<diff:
                    print("In here")
                    nums[x+1]= nums[x]
                    diff = nums[x+1]-nums[x]
                    count = count+1
                    print("",nums)
                    break
        
        print("heya")
        for y in range(len(nums)):
                if y+1 < len(nums):
                    if nums[y+1]-nums[y] < 0:
                        print("In here if")
                        flag = True
                        if flag == True:
                            return False
                    else:
                        continue
        return True

sol  = Solution()
nums = [2,3,3,2,4]
l = sol.checkPossibility(nums)
print("",l)

