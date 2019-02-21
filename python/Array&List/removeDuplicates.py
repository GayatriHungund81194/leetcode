class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        
        x=0
        y=x+1
        while(x<len(nums)):
            if nums[x]==nums[x-1]:
                nums.remove(nums[x])
                x = x+1
            else:
                x=x+1
            
        return nums

sol  = Solution()
nums = [0,1,1,2]
l = sol.removeDuplicates(nums)
print("",l)
        