class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        b = 0
        
        n = len(nums)
        l = nums[::-1]
        print("l:",l)
        for i in range(0, (int)(k/2)): 
            temp = nums[i] 
            nums[i] = nums[k-i-1] 
            nums[k-i-1] = temp 
        for i in range((int)(k/2)-1,len(nums)-1): 
            temp = nums[i] 
            nums[i] = nums[k-i-1] 
            nums[k-i-1] = temp 
        #for y in range(len(nums)):
         #   n = m[::-1]
        return nums


sol  = Solution()
nums = [2,5,5,11]
l = sol.rotate(nums,3)
print("",l)