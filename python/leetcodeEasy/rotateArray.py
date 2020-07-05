class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        temp=0
        y=1
        while y!=k:
            last  = nums[len(nums)-1]
            for x in range(len(nums)):
                temp = nums[x]
                nums[x] = last
                last=temp
            return nums
sol=Solution()
arr = [1,2,3,4,5,6,7]
ans= sol.rotate(arr,4)
print("",ans)
        