class Solution:
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        i=0
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return i 



sol  = Solution()
nums = [0,1,0]
l = sol.peakIndexInMountainArray(nums)
print("",l)