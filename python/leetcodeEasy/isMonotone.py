class Solution:
    def isMonotonic(self, A: 'List[int]') -> 'bool':
        flag = True
        flag2 = True
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                flag = False
            if A[i] < A[i+1]:
                flag2=False
        return flag or flag2
            

sol  = Solution()
nums = [1,2,2,3]
l = sol.isMonotonic(nums)
print("",l)