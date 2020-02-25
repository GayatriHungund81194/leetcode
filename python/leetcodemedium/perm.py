class Solution:
    def permute(self, nums):
        def permutation(nums,seen):
            if len(nums)==2:
                seen.append([nums[0],nums[1]])
                seen.append([nums[1],nums[0]])
                return
            for x in range(len(nums)):
                seen=[]
                seen.append(nums[x])
                permutation(nums[x+1:],seen)

        permutation(nums,[])

sol=Solution()
sol.permute([1,2,3])


